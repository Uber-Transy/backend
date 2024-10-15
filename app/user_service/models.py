# ---------- Imports ---------
import enum
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import Email, ValidationError

db = SQLAlchemy()

# ---------- Validators ----------
def validate_email_format(email):
    try:
        Email()(None, email)
    except ValidationError:
        raise ValueError(f"Invalid email format: {email}")

# ---------- Models ----------
class UserRole(enum.Enum):
    DRIVER = "driver"
    GUARDIAN = "guardian"
    SCHOOL = "school"

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    full_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(280), nullable=False)  
    role = db.Column(db.Enum(UserRole), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    driver = db.relationship('Driver', uselist=False, backref='user')
    guardian = db.relationship('Guardian', uselist=False, backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email}>"

    @staticmethod
    def validate_email(email):
        validate_email_format(email)

    @classmethod
    def create(cls, full_name, email, phone_number, password, role):
        cls.validate_email(email)
        user = cls(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            role=role
        )
        user.set_password(password)
        return user


class Guardian(db.Model):
    __tablename__ = 'guardian'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    students = db.relationship('Student', backref='guardian', lazy=True)

    def __repr__(self):
        return f"<Guardian {self.id}>"


class Driver(db.Model):
    __tablename__ = 'driver'

    id = db.Column(db.Integer, primary_key=True)
    driving_license = db.Column(db.String(100), nullable=False)
    id_card = db.Column(db.String(100), nullable=False)
    unique_identifier = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User

    vehicles = db.relationship('Vehicle', backref='driver', lazy=True)  # One-to-many relationship with Vehicle

    def __repr__(self):
        return f"<Driver {self.unique_identifier}>"


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    Date_of_birth = db.Column(db.String(50), nullable=False)
    school_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    unique_identifier = db.Column(db.String(50), nullable=False)

    guardian = db.Column(db.Integer, db.ForeignKey('guardian.id'), nullable=False)

    def __repr__(self):
        return f"<Student {self.unique_identifier}>"


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    registration_number = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    vehicle_details = db.Column(JSON, nullable=True)

    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)  # Foreign key to Driver

    def __repr__(self):
        return f"<Vehicle {self.registration_number}>"