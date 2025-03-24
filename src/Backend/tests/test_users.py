import pytest

def test_book_slot_success(client, auth_headers, test_barber):
    # Test booking an available slot
    response = client.post(
        "/api/users/book", 
        headers=auth_headers,
        json={
            "barber_id": test_barber["id"],
            "time": "2025-04-01T10:00"  # This is an available slot from our fixture
        }
    )
    
    assert response.status_code == 201
    assert response.json["message"] == "Appointment booked successfully"
    
    # Verify the slot is now booked
    slots_response = client.get(f"/api/barber/{test_barber['id']}/slots")
    slots = slots_response.json
    
    for slot in slots:
        if slot["time"] == "2025-04-01T10:00":
            assert slot["booked"] == True
            break

def test_book_already_booked_slot(client, auth_headers, test_barber):
    # Test booking a slot that's already booked
    response = client.post(
        "/api/users/book", 
        headers=auth_headers,
        json={
            "barber_id": test_barber["id"],
            "time": "2025-04-01T11:00"  # This is already booked in our fixture
        }
    )
    
    assert response.status_code == 400
    assert response.json["error"] == "Slot not available"

def test_book_missing_fields(client, auth_headers):
    # Test booking with missing fields
    response = client.post(
        "/api/users/book", 
        headers=auth_headers,
        json={
            "barber_id": "some_id"
            # Missing time field
        }
    )
    
    assert response.status_code == 400
    assert response.json["error"] == "Missing required fields"

def test_cancel_appointment(client, auth_headers, test_barber, test_user, app):
    # First, ensure we have a booked appointment to cancel
    with app.app_context():
        from api import mongo
        from bson.objectid import ObjectId
        
        # Book a slot directly in the database
        mongo.db.barbers.update_one(
            {"_id": ObjectId(test_barber["id"]), "available_slots.time": "2025-04-01T10:00"},
            {"$set": {"available_slots.$.booked": True, "available_slots.$.user_id": ObjectId(test_user["id"])}}
        )
        
        mongo.db.users.update_one(
            {"_id": ObjectId(test_user["id"])},
            {"$push": {"booked_slots": {"barber_id": test_barber["id"], "time": "2025-04-01T10:00"}}}
        )
    
    # Now test cancellation
    response = client.post(
        "/api/users/cancel", 
        headers=auth_headers,
        json={
            "barber_id": test_barber["id"],
            "time": "2025-04-01T10:00"
        }
    )
    
    assert response.status_code == 200
    assert response.json["message"] == "Appointment canceled successfully"
    
    # Verify the slot is now available
    slots_response = client.get(f"/api/barber/{test_barber['id']}/slots")
    slots = slots_response.json
    
    for slot in slots:
        if slot["time"] == "2025-04-01T10:00":
            assert slot["booked"] == False
            assert slot["user_id"] is None
            break

def test_cancel_missing_fields(client, auth_headers):
    # Test cancelling with missing fields
    response = client.post(
        "/api/users/cancel", 
        headers=auth_headers,
        json={
            # Missing required fields
        }
    )
    
    assert response.status_code == 400
    assert response.json["error"] == "Missing required fields"

def test_jwt_protection(client, auth_headers):
    # Test the JWT protection works
    response = client.get("/api/users/test", headers=auth_headers)
    
    assert response.status_code == 200
    assert response.json["message"] == "JWT is working!"
    
    # Test without headers
    response_without_auth = client.get("/api/users/test")
    assert response_without_auth.status_code in [401, 422]  # Unauthorized or missing token