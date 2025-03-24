import pytest
import json
from flask import Flask

def test_register_user(client):
    # Test user registration
    response = client.post("/api/auth/register/user", json={
        "name": "New User",
        "email": "new@user.com",
        "password": "password123"
    })
    
    assert response.status_code == 201
    assert "user_id" in response.json
    assert response.json["message"] == "User registered"

def test_register_duplicate_user(client):
    # Register a user
    client.post("/api/auth/register/user", json={
        "name": "Duplicate User",
        "email": "duplicate@user.com",
        "password": "password123"
    })
    
    # Try to register with the same email
    response = client.post("/api/auth/register/user", json={
        "name": "Duplicate User",
        "email": "duplicate@user.com",
        "password": "password456"
    })
    
    assert response.status_code == 400
    assert response.json["error"] == "Email already registered"

def test_register_barber(client):
    # Test barber registration
    response = client.post("/api/auth/register/barber", json={
        "name": "New Barber",
        "email": "new@barber.com",
        "password": "password123"
    })
    
    assert response.status_code == 201
    assert "barber_id" in response.json
    assert response.json["message"] == "Barber registered"

def test_login_user_success(client):
    # Register a user first
    client.post("/api/auth/register/user", json={
        "name": "Login User",
        "email": "login@user.com",
        "password": "password123"
    })
    
    # Test successful login
    response = client.post("/api/auth/login/user", json={
        "email": "login@user.com",
        "password": "password123"
    })
    
    assert response.status_code == 200
    assert "access_token" in response.json
    assert "user_id" in response.json
    assert response.json["role"] == "customer"

def test_login_user_invalid_credentials(client):
    # Test login with wrong password
    response = client.post("/api/auth/login/user", json={
        "email": "test@user.com",
        "password": "wrongpassword"
    })
    
    assert response.status_code == 401
    assert response.json["error"] == "Invalid credentials"

def test_login_barber_success(client):
    # Register a barber first
    client.post("/api/auth/register/barber", json={
        "name": "Login Barber",
        "email": "login@barber.com",
        "password": "password123"
    })
    
    # Test successful login
    response = client.post("/api/auth/login/barber", json={
        "email": "login@barber.com",
        "password": "password123"
    })
    
    assert response.status_code == 200
    assert "access_token" in response.json
    assert "barber_id" in response.json
    assert response.json["role"] == "barber"

def test_protected_route(client, auth_headers):
    # Test accessing a protected route with a valid token
    response = client.get("/api/auth/test", headers=auth_headers)
    
    assert response.status_code == 200
    assert response.json["message"] == "Token is valid"