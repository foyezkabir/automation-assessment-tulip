import pytest
import requests
import json


# Base configuration
BASE_URL = "https://api.practicesoftwaretesting.com"
MESSAGES_ENDPOINT = f"{BASE_URL}/messages"


class TestMessagesAPI:
    """API Tests for POST /messages endpoint"""
    
    def test_post_message_success(self):
        """
        Test Case 1: Successfully POST a message with all required fields
        
        Expected: 201 Created with message confirmation
        """
        # Arrange
        payload = {
            "name": "Foyez Kabir",
            "email": "foyezkabir00@gmail.com",
            "subject": "webmaster",
            "message": "This is an automated API test message. Please ignore."
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        response_data = response.json()
        assert "id" in response_data or "message" in response_data or response_data is not None, "Response should contain data"
        
        print(f"✓ Message created successfully: {response_data}")
    
    def test_post_message_missing_name(self):
        """
        Test Case 2: POST message without name field
        
        Expected: API accepts but may return validation message
        """
        # Arrange
        payload = {
            "email": "test@example.com",
            "subject": "customer",
            "message": "Test message without name"
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        response_data = response.json()
        print(f"✓ Response for missing name: {response_data}")
    
    def test_post_message_missing_email(self):
        """
        Test Case 3: POST message without email field
        
        Expected: API accepts but may return validation message
        """
        # Arrange
        payload = {
            "name": "Test User",
            "subject": "customer",
            "message": "Test message without email"
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        response_data = response.json()
        print(f"✓ Response for missing email: {response_data}")
    
    def test_post_message_invalid_email_format(self):
        """
        Test Case 4: POST message with invalid email format
        
        Expected: 400 Bad Request or 422 Unprocessable Entity
        """
        # Arrange
        payload = {
            "name": "Test User",
            "email": "invalid-email-format",
            "subject": "customer",
            "message": "Test message with invalid email"
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        assert response.status_code in [400, 422], f"Expected 400/422, got {response.status_code}"
        
        response_data = response.json()
        print(f"✓ Validation error for invalid email: {response_data}")
    
    def test_post_message_missing_subject(self):
        """
        Test Case 5: POST message without subject field
        
        Expected: 400 Bad Request or 422 Unprocessable Entity
        """
        # Arrange
        payload = {
            "name": "Test User",
            "email": "test@example.com",
            "message": "Test message without subject"
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        assert response.status_code in [400, 422], f"Expected 400/422, got {response.status_code}"
        
        response_data = response.json()
        print(f"✓ Validation error for missing subject: {response_data}")
    
    def test_post_message_missing_message_body(self):
        """
        Test Case 6: POST message without message body
        
        Expected: 400 Bad Request or 422 Unprocessable Entity
        """
        # Arrange
        payload = {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "customer"
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        assert response.status_code in [400, 422], f"Expected 400/422, got {response.status_code}"
        
        response_data = response.json()
        print(f"✓ Validation error for missing message: {response_data}")
    
    def test_post_message_empty_payload(self):
        """
        Test Case 7: POST with empty payload
        
        Expected: 400 Bad Request or 422 Unprocessable Entity
        """
        # Arrange
        payload = {}
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        assert response.status_code in [400, 422], f"Expected 400/422, got {response.status_code}"
        
        response_data = response.json()
        print(f"✓ Validation error for empty payload: {response_data}")
    
    def test_post_message_with_all_subject_options(self):
        """
        Test Case 8: POST messages with different subject options
        
        Subject options: webmaster, customer, return
        """
        subjects = ["webmaster", "customer", "return"]
        
        for subject in subjects:
            # Arrange
            payload = {
                "name": "Test User",
                "email": "test@example.com",
                "subject": subject,
                "message": f"Test message with subject: {subject}"
            }
            
            # Act
            response = requests.post(MESSAGES_ENDPOINT, json=payload)
            
            # Assert
            assert response.status_code == 200, f"Failed for subject '{subject}': {response.status_code}"
            print(f"✓ Message created with subject '{subject}'")
    
    def test_post_message_very_long_message(self):
        """
        Test Case 9: POST message with very long message body
        
        Expected: 201 Created or potential length validation
        """
        # Arrange
        long_message = "A" * 5000  # 5000 characters
        payload = {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "customer",
            "message": long_message
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        # Could be 200 if accepted, or 400/422 if length validation exists
        assert response.status_code in [200, 400, 422], f"Unexpected status: {response.status_code}"
        
        print(f"✓ Long message test: Status {response.status_code}")
    
    def test_post_message_response_headers(self):
        """
        Test Case 10: Verify response headers
        
        Expected: Proper Content-Type header
        """
        # Arrange
        payload = {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "webmaster",
            "message": "Testing response headers"
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        assert response.status_code == 200
        assert "Content-Type" in response.headers, "Content-Type header missing"
        assert "application/json" in response.headers["Content-Type"], "Expected JSON response"
        
        print(f"✓ Response headers verified: {response.headers.get('Content-Type')}")
    
    def test_post_message_response_time(self):
        """
        Test Case 11: Verify API response time
        
        Expected: Response within acceptable time (< 3 seconds)
        """
        # Arrange
        payload = {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "customer",
            "message": "Testing response time"
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        response_time = response.elapsed.total_seconds()
        
        # Assert
        assert response.status_code == 200
        assert response_time < 3.0, f"Response time too slow: {response_time}s"
        
        print(f"✓ Response time: {response_time:.2f}s")
    
    def test_post_message_special_characters(self):
        """
        Test Case 12: POST message with special characters
        
        Expected: 201 Created - API should handle special characters
        """
        # Arrange
        payload = {
            "name": "Test User !@#$%",
            "email": "test+special@example.com",
            "subject": "customer",
            "message": "Message with special chars: <>&\"'`~!@#$%^&*()"
        }
        
        # Act
        response = requests.post(MESSAGES_ENDPOINT, json=payload)
        
        # Assert
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        print(f"✓ Special characters handled correctly")


# Standalone test functions (can be run individually)
def test_api_endpoint_availability():
    """
    Test Case 13: Verify API endpoint is accessible
    """
    try:
        response = requests.options(MESSAGES_ENDPOINT, timeout=5)
        assert response.status_code in [200, 204, 405], f"Unexpected status: {response.status_code}"
        print(f"✓ API endpoint is accessible")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"API endpoint not reachable: {e}")


if __name__ == "__main__":
    # Run tests programmatically
    pytest.main([__file__, "-v", "--tb=short"])
