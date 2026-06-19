"""
Tests for the signup endpoint (POST /activities/{activity_name}/signup).

Verify that students can successfully sign up for activities.
"""


def test_signup_for_activity_adds_participant(test_client):
    """
    Arrange: sample_activities fixture provides activities with existing participants
    
    Act: Sign up a new student for an activity
    
    Assert: Verify the participant is added to the activity
    """
    # Arrange
    activity_name = "Chess Club"
    new_email = "newstudent@mergington.edu"
    initial_count = len(test_client.get("/activities").json()[activity_name]["participants"])
    
    # Act
    response = test_client.post(
        f"/activities/{activity_name}/signup",
        params={"email": new_email}
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {new_email} for {activity_name}"
    
    # Verify participant was actually added
    activities = test_client.get("/activities").json()
    assert new_email in activities[activity_name]["participants"]
    assert len(activities[activity_name]["participants"]) == initial_count + 1


def test_signup_for_activity_returns_success_message(test_client):
    """
    Arrange: sample_activities fixture is ready
    
    Act: Sign up a new student for Programming Class
    
    Assert: Verify the response contains the correct success message
    """
    # Act
    response = test_client.post(
        "/activities/Programming Class/signup",
        params={"email": "alex@mergington.edu"}
    )
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "alex@mergington.edu" in data["message"]
    assert "Programming Class" in data["message"]


def test_signup_for_multiple_activities(test_client):
    """
    Arrange: sample_activities fixture with multiple activities
    
    Act: Sign up a student for two different activities
    
    Assert: Verify the student appears in both activity participant lists
    """
    # Arrange
    student_email = "versatile@mergington.edu"
    activities = ["Chess Club", "Programming Class"]
    
    # Act
    for activity_name in activities:
        response = test_client.post(
            f"/activities/{activity_name}/signup",
            params={"email": student_email}
        )
        assert response.status_code == 200
    
    # Assert
    all_activities = test_client.get("/activities").json()
    for activity_name in activities:
        assert student_email in all_activities[activity_name]["participants"]
