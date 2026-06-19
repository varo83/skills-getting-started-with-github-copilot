"""
Test configuration and fixtures for the Mergington High School API.

This module provides pytest fixtures for testing the FastAPI application
with isolated, controlled test data.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def sample_activities():
    """
    Fixture: Sample activities data with controlled state for testing.
    
    Returns a fresh copy of activities for each test to ensure test isolation
    and prevent cross-test dependencies.
    """
    return {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Team drills, games, and coaching for competitive basketball",
            "schedule": "Mondays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 15,
            "participants": ["tyler@mergington.edu", "nina@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Lap swimming, strokes, and water safety practice",
            "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["laura@mergington.edu", "matt@mergington.edu"]
        },
        "Art Club": {
            "description": "Drawing, painting, and creative projects for students",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["oliver@mergington.edu", "mia@mergington.edu"]
        },
        "Drama Club": {
            "description": "Acting, stage production, and theater workshops",
            "schedule": "Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["zoe@mergington.edu", "ethan@mergington.edu"]
        },
        "Science Club": {
            "description": "Hands-on experiments and science fair preparation",
            "schedule": "Mondays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["sara@mergington.edu", "jake@mergington.edu"]
        },
        "Debate Team": {
            "description": "Research, public speaking, and competitive debate practice",
            "schedule": "Wednesdays and Fridays, 4:30 PM - 6:00 PM",
            "max_participants": 16,
            "participants": ["linda@mergington.edu", "alex@mergington.edu"]
        }
    }


@pytest.fixture
def test_client(sample_activities, monkeypatch):
    """
    Fixture: TestClient with isolated activities data.
    
    Uses monkeypatch to replace the app's global activities dict with
    the sample_activities fixture, ensuring each test runs with fresh data
    and doesn't affect other tests.
    """
    # Replace the app's activities with our isolated fixture data
    monkeypatch.setattr("src.app.activities", sample_activities)
    
    # Return a test client that can make HTTP requests to the app
    return TestClient(app)
