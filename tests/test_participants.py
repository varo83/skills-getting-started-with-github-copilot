"""
Tests for the participant removal endpoint (DELETE /activities/{activity_name}/participants).

Verify that students can be unregistered from activities.
"""


def test_unregister_participant_removes_from_activity(test_client):
    """
    Arrange: sample_activities fixture has participants already registered
    
    Act: Unregister an existing participant from an activity
    
    Assert: Verify the participant is removed from the activity
    """
    # Arrange
    activity_name = "Chess Club"
    email_to_remove = "michael@mergington.edu"
    initial_count = len(test_client.get("/activities").json()[activity_name]["participants"])
    
    # Act
    response = test_client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email_to_remove}
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email_to_remove} from {activity_name}"
    
    # Verify participant was actually removed
    activities = test_client.get("/activities").json()
    assert email_to_remove not in activities[activity_name]["participants"]
    assert len(activities[activity_name]["participants"]) == initial_count - 1


def test_unregister_participant_returns_success_message(test_client):
    """
    Arrange: sample_activities fixture with participants
    
    Act: Unregister a participant from Programming Class
    
    Assert: Verify the response contains the correct message
    """
    # Act
    response = test_client.delete(
        "/activities/Programming Class/participants",
        params={"email": "emma@mergington.edu"}
    )
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "emma@mergington.edu" in data["message"]
    assert "Programming Class" in data["message"]


def test_unregister_multiple_participants(test_client):
    """
    Arrange: sample_activities fixture with multiple participants
    
    Act: Unregister multiple participants from the same activity
    
    Assert: Verify all participants are correctly removed
    """
    # Arrange
    activity_name = "Basketball Team"
    participants_to_remove = ["tyler@mergington.edu", "nina@mergington.edu"]
    
    # Act
    for email in participants_to_remove:
        response = test_client.delete(
            f"/activities/{activity_name}/participants",
            params={"email": email}
        )
        assert response.status_code == 200
    
    # Assert
    all_activities = test_client.get("/activities").json()
    for email in participants_to_remove:
        assert email not in all_activities[activity_name]["participants"]
    
    # Verify activity is now empty (or has zero participants)
    assert len(all_activities[activity_name]["participants"]) == 0
