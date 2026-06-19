"""
Tests for the activities endpoint (GET /activities).

Verify that the API returns all available activities with correct structure.
"""


def test_get_activities_returns_all_activities(test_client):
    """
    Arrange: sample_activities fixture provides 9 activities
    
    Act: Make a GET request to /activities
    
    Assert: Verify all activities are returned with correct structure
    """
    # Act
    response = test_client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    
    # Verify we got all 9 activities
    assert len(data) == 9
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data
    assert "Basketball Team" in data
    assert "Swimming Club" in data
    assert "Art Club" in data
    assert "Drama Club" in data
    assert "Science Club" in data
    assert "Debate Team" in data


def test_get_activities_has_correct_structure(test_client):
    """
    Arrange: sample_activities fixture provides activities data
    
    Act: Make a GET request to /activities and inspect an activity
    
    Assert: Verify each activity has required fields
    """
    # Act
    response = test_client.get("/activities")
    data = response.json()
    
    # Assert - verify Chess Club has all required fields
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    
    # Verify types
    assert isinstance(chess_club["description"], str)
    assert isinstance(chess_club["schedule"], str)
    assert isinstance(chess_club["max_participants"], int)
    assert isinstance(chess_club["participants"], list)


def test_get_activities_includes_participant_data(test_client):
    """
    Arrange: sample_activities fixture includes participant data
    
    Act: Make a GET request to /activities
    
    Assert: Verify participants are correctly listed
    """
    # Act
    response = test_client.get("/activities")
    data = response.json()
    
    # Assert - Chess Club should have 2 participants
    assert len(data["Chess Club"]["participants"]) == 2
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in data["Chess Club"]["participants"]
