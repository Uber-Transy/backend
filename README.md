# 🚀 Uber for Teens - Secure Pickup & Tracking App

This project is a mobile application that allows parents to arrange secure transportation for their teens / students and track their movement in real-time. It is designed to provide peace of mind to parents by monitoring and ensuring that teens get home safely from school or other activities.

The backend is built with **Flask** and handles API requests, user authentication, and real-time tracking, while the frontend is developed using **React Native**, providing a cross-platform mobile app experience.

## 🛠 Tech Stack

### Backend (API)
- **Flask**: Python microframework for handling HTTP requests and backend logic.
- **Flask-Restful**: For creating RESTful APIs.
- **Flask-JWT-Extended**: For secure user authentication with JWT tokens.
- **SQLAlchemy**: ORM for interacting with the database.
- **PostgreSQL**: Database for storing user information, trip details, etc.
- **Flask-SocketIO**: For real-time communication (e.g., live tracking of the teen's location).

### Frontend (Mobile App)
- **React Native**: For building the cross-platform mobile application (iOS & Android).
- **React Navigation**: Navigation system for the app.
- **Redux**: State management for handling app-wide states (e.g., user authentication, trip data).
- **Axios**: HTTP client for making API requests to the Flask backend.
- **Socket.IO**: For real-time tracking of the teen’s location on the app.
- **Google Maps API**: For rendering the map and showing the teen’s location.

## 🌟 Features

1. **User Roles**:
   - **Parents**: Can schedule rides, track their teens, and view trip history.
   - **Teens**: Can view ride details, estimated arrival time, and notify parents when they arrive.
   - **Drivers**: Assigned to pick up teens and responsible for safely transporting them.

2. **Secure Authentication**:
   - Users (Parents, Teens, Drivers) can register and log in using secure JWT authentication.

3. **Real-Time Tracking**:
   - Parents can track their teen's live location from school to home in real-time via the app.

4. **Ride Scheduling**:
   - Parents can schedule rides for their teens and receive notifications when the driver is on the way and when the teen has arrived.

5. **Notifications**:
   - Push notifications to alert parents when the ride has started, during transit, and when the teen reaches home.

6. **Payment Integration**:
   - Parents can securely pay for rides through integrated payment gateways.

7. **Data Protection**:
   - Ensure compliance with data protection regulations, keeping all user data secure.

## 🏁 Getting Started

### Prerequisites

- **Node.js** (for React Native): Install from [Node.js website](https://nodejs.org/)
- **Python 3.9+** (for Flask backend): Install from [Python website](https://www.python.org/downloads/)
- **PostgreSQL**: Install from [PostgreSQL website](https://www.postgresql.org/download/)
- **React Native CLI**: Install via npm: `npm install -g react-native-cli`
- **Expo** (optional): Install via npm: `npm install -g expo-cli`

### Backend Setup (Flask)

1. Clone the repository:
   ```bash
   git clone https://github.com/Uber-Transy/backend.git
   cd backend
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. Install dependencies:
   ```bash
   pip install -r requiremenents.txt
4. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
5. Run the flask development server:
   ```bash
   flask run

## 🔗 API Endpoints

### Auth

- **POST /auth/register**: Register a new user (Parent, Teen, Driver).
- **POST /auth/login**: Login and receive JWT token.
   
## 🤝 Contributing
We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a feature branch (git checkout -b feature-name).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature-name).
5. Open a pull request.

## 📫 Contact
For any inquiries, please contact us at [jeffowen04@gmail.com].
