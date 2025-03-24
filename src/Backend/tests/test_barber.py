import pytest

def test_add_slots_success(client, barber_auth_headers, test_barber):
    # Test adding time slots as the authorized barber
    response = client.post(
        f"/api/barber/{test_barber['id']}/slots", 
        headers=barber_auth_headers,
        json={"slots": ["2025-04-02T09:00", "2025-04-02T10:00", "2025-04-02T11:00"]}
    )
    
    assert response.status_code == 201
    assert response.json["message"] == "Slots added successfully"
    
    # Verify slots were added
    get_response = client.get(f"/api/barber/{test_barber['id']}/slots")
    slots = get_response.json
    
    # Check that our new slots are in the list
    slot_times = [slot["time"] for slot in slots]
    assert "2025-04-02T09:00" in slot_times
    assert "2025-04-02T10:00" in slot_times
    assert "2025-04-02T11:00" in slot_times

def test_add_slots_unauthorized(client, auth_headers, test_barber):
    # Test adding slots as a different user (not the barber)
    response = client.post(
        f"/api/barber/{test_barber['id']}/slots", 
        headers=auth_headers,  # Using regular user auth
        json={"slots": ["2025-04-03T09:00"]}
    )
    
    assert response.status_code == 403
    assert response.json["error"] == "Unauthorized"

def test_add_slots_invalid_format(client, barber_auth_headers, test_barber):
    # Test adding slots with invalid format
    response = client.post(
        f"/api/barber/{test_barber['id']}/slots", 
        headers=barber_auth_headers,
        json={"invalid_key": "invalid_value"}
    )
    
    assert response.status_code == 400
    assert "error" in response.json

def test_get_available_slots(client, test_barber):
    # Test getting all slots for a barber
    response = client.get(f"/api/barber/{test_barber['id']}/slots")
    
    assert response.status_code == 200
    assert isinstance(response.json, list)
    
    # Verify structure of slots
    if len(response.json) > 0:
        slot = response.json[0]
        assert "time" in slot
        assert "booked" in slot

def test_get_slots_nonexistent_barber(client):
    # Test getting slots for a barber that doesn't exist
    fake_id = "123456789012345678901234"  # 24-character hex string
    response = client.get(f"/api/barber/{fake_id}/slots")
    
    assert response.status_code == 404
    assert response.json["error"] == "Barber not found"