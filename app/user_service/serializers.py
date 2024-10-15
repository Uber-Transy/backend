# ---------- Imports ---------
from marshmallow import Schema, fields, validate, validates, ValidationError
from marshmallow_enum import EnumField
from .models import UserRole, User, Guardian, Driver, Student, Vehicle

# ---------- Validators ----------
def validate_email_format(email):
    if not validate.Email()(email):
        raise ValidationError("Invalid email format.")

# ---------- Schemas ----------

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    full_name = fields.Str(required=True, validate=validate.Length(max=50))
    email = fields.Email(required=True, validate=validate.Length(max=50))
    phone_number = fields.Str(required=True, validate=validate.Length(max=20))
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
    role = EnumField(UserRole, by_value=True, required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    driver = fields.Nested('DriverSchema', dump_only=True)
    guardian = fields.Nested('GuardianSchema', dump_only=True)

    @validates('email')
    def validate_email(self, value):
        validate_email_format(value)

    def create_user(self, data):
        user = User(
            full_name=data['full_name'],
            email=data['email'],
            phone_number=data['phone_number'],
            role=data['role']
        )
        user.set_password(data['password'])
        return user

class GuardianSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    students = fields.List(fields.Nested('StudentSchema'), dump_only=True)

    class Meta:
        fields = ('id', 'user_id', 'students')

class DriverSchema(Schema):
    id = fields.Int(dump_only=True)
    driving_license = fields.Str(required=True, validate=validate.Length(max=100))
    id_card = fields.Str(required=True, validate=validate.Length(max=100))
    unique_identifier = fields.Str(required=True, validate=validate.Length(max=100))
    user_id = fields.Int(required=True)
    vehicles = fields.List(fields.Nested('VehicleSchema'), dump_only=True)

    class Meta:
        fields = ('id', 'driving_license', 'id_card', 'unique_identifier', 'user_id', 'vehicles')

class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    full_name = fields.Str(required=True, validate=validate.Length(max=50))
    Date_of_birth = fields.Str(required=True, validate=validate.Length(max=50))
    school_name = fields.Str(required=True, validate=validate.Length(max=100))
    gender = fields.Str(required=True, validate=validate.OneOf(["male", "female"]))
    unique_identifier = fields.Str(required=True, validate=validate.Length(max=50))
    guardian = fields.Int(required=True)

    class Meta:
        fields = ('id', 'full_name', 'Date_of_birth', 'school_name', 'gender', 'unique_identifier', 'guardian')

class VehicleSchema(Schema):
    id = fields.Int(dump_only=True)
    registration_number = fields.Str(required=True, validate=validate.Length(max=50))
    model = fields.Str(required=True, validate=validate.Length(max=100))
    color = fields.Str(required=True, validate=validate.Length(max=50))
    vehicle_details = fields.Dict()  # For JSON field
    driver_id = fields.Int(required=True)

    class Meta:
        fields = ('id', 'registration_number', 'model', 'color', 'vehicle_details', 'driver_id')

