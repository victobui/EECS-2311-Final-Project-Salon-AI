import pytest
import sys
import os
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from bson.objectid import ObjectId

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from api import create_app, mongo

@pytest.fixture
def app():
    # Configure the app for testing
    app = create_app({"TESTING": True, 
                      "MONGO_URI": "mongodb://localhost:27017/salon_test",
                      "JWT_SECRET_KEY": "test_secret_key"})
    
    # Create an application context
    with app.app_context():
        # Clear the test database
        mongo.db.users.delete_many({})
        mongo.db.barbers.delete_many({})
        
        # Create a test user and barber
        bcrypt = Bcrypt(app)
        test_password_hash = bcrypt.generate_password_hash("testpassword").decode("utf-8")
        
        test_user_id = mongo.db.users.insert_one({
            "name": "Test User",
            "email": "test@user.com",
            "password": test_password_hash,
            "role": "customer",
            "booked_slots": []
        }).inserted_id
        
        test_barber_id = mongo.db.barbers.insert_one({
            "name": "Test Barber",
            "email": "test@barber.com",
            "password": test_password_hash,
            "role": "barber",
            "available_slots": [
                {"time": "2025-04-01T10:00", "booked": False, "user_id": None},
                {"time": "2025-04-01T11:00", "booked": True, "user_id": test_user_id}
            ]
        }).inserted_id
        
    yield app
    
    # Clean up after tests
    with app.app_context():
        mongo.db.users.delete_many({})
        mongo.db.barbers.delete_many({})

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_user(app):
    with app.app_context():
        user = mongo.db.users.find_one({"email": "test@user.com"})
        return {
            "id": str(user["_id"]),
            "email": user["email"]
        }

@pytest.fixture
def test_barber(app):
    with app.app_context():
        barber = mongo.db.barbers.find_one({"email": "test@barber.com"})
        return {
            "id": str(barber["_id"]),
            "email": barber["email"]
        }

@pytest.fixture
def auth_headers(client, test_user):
    # Log in the test user
    response = client.post("/api/auth/login/user", json={
        "email": test_user["email"],
        "password": "testpassword"
    })
    token = response.json["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def barber_auth_headers(client, test_barber):
    # Log in the test barber
    response = client.post("/api/auth/login/barber", json={
        "email": test_barber["email"],
        "password": "testpassword"
    })
    token = response.json["access_token"]
    return {"Authorization": f"Bearer {token}"}