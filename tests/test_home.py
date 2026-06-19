"""
Tests for the home endpoint (GET /).

Verify that the root endpoint redirects to the static homepage.
"""


def test_root_redirects_to_static_homepage(test_client):
    """
    Arrange: No setup needed (root endpoint has no dependencies)
    
    Act: Make a GET request to the root endpoint
    
    Assert: Verify the response redirects to /static/index.html
    """
    # Act
    response = test_client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == 307  # Temporary redirect
    assert response.headers["location"] == "/static/index.html"
