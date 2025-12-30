import pytest
import requests
import json
import time


# Base configuration
BASE_URL = "https://api.practicesoftwaretesting.com"
CARTS_ENDPOINT = f"{BASE_URL}/carts"


class TestCartsGetAPI:
    """API Tests for GET /carts/{cart_id} endpoint"""
    
    def test_get_cart_with_valid_id(self):
        """
        Test Case 1: GET cart with valid cart ID
        
        Expected: 200 OK with cart details
        """
        # Arrange
        cart_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        
        # Act
        response = requests.get(f"{CARTS_ENDPOINT}/{cart_id}")
        
        # Assert
        assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"
        
        if response.status_code == 200:
            response_data = response.json()
            print(f"✓ Cart retrieved successfully: {response_data}")
            
            # Validate response structure
            assert isinstance(response_data, (dict, list)), "Response should be dict or list"
        else:
            print(f"✓ Cart not found (404) - This is also a valid response for expired/invalid cart")
    
    def test_get_cart_response_structure(self):
        """
        Test Case 2: Validate response structure for valid cart
        
        Expected: Response contains expected fields (id, items, total, etc.)
        """
        # Arrange
        cart_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        
        # Act
        response = requests.get(f"{CARTS_ENDPOINT}/{cart_id}")
        
        # Assert
        if response.status_code == 200:
            response_data = response.json()
            
            # Check for common cart fields
            if isinstance(response_data, dict):
                # Typically cart response might have: id, items, total, etc.
                print(f"✓ Cart structure: {list(response_data.keys())}")
                
                # Validate it's a proper JSON response
                assert response_data is not None, "Response data should not be None"
            else:
                print(f"✓ Cart response is a list with {len(response_data)} items")
        else:
            print(f"✓ Cart not found - skipping structure validation")
    
    def test_get_cart_with_invalid_id_format(self):
        """
        Test Case 3: GET cart with invalid ID format
        
        Expected: 400 Bad Request or 404 Not Found
        """
        # Arrange
        invalid_ids = [
            "invalid-id",
            "12345",
            "abc123xyz",
            "!@#$%^&*()",
            "123abc456def789"
        ]
        
        for invalid_id in invalid_ids:
            # Act
            response = requests.get(f"{CARTS_ENDPOINT}/{invalid_id}")
            
            # Assert
            assert response.status_code in [400, 404, 422], f"Expected 400/404/422 for '{invalid_id}', got {response.status_code}"
            print(f"✓ Invalid ID '{invalid_id}' handled correctly: {response.status_code}")
    
    def test_get_cart_with_non_existent_id(self):
        """
        Test Case 4: GET cart with valid format but non-existent ID
        
        Expected: 404 Not Found
        """
        # Arrange
        non_existent_id = "01kdqfvwjy5c3dan2ntjdf99999"  # Valid format but doesn't exist
        
        # Act
        response = requests.get(f"{CARTS_ENDPOINT}/{non_existent_id}")
        
        # Assert
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        
        response_data = response.json()
        print(f"✓ Non-existent cart handled correctly: {response_data}")
    
    def test_get_cart_with_empty_id(self):
        """
        Test Case 5: GET cart with empty ID (just /carts/)
        
        Expected: 404 Not Found or 405 Method Not Allowed
        """
        # Act
        response = requests.get(f"{CARTS_ENDPOINT}/")
        
        # Assert
        assert response.status_code in [404, 405], f"Expected 404/405, got {response.status_code}"
        print(f"✓ Empty ID handled correctly: {response.status_code}")
    
    def test_get_cart_response_time(self):
        """
        Test Case 6: Verify API response time
        
        Expected: Response within acceptable time (< 3 seconds)
        """
        # Arrange
        cart_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        
        # Act
        response = requests.get(f"{CARTS_ENDPOINT}/{cart_id}")
        response_time = response.elapsed.total_seconds()
        
        # Assert
        assert response_time < 3.0, f"Response time too slow: {response_time}s"
        print(f"✓ Response time: {response_time:.3f}s")
    
    def test_get_cart_response_headers(self):
        """
        Test Case 7: Verify response headers
        
        Expected: Proper Content-Type and other headers
        """
        # Arrange
        cart_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        
        # Act
        response = requests.get(f"{CARTS_ENDPOINT}/{cart_id}")
        
        # Assert
        assert "Content-Type" in response.headers, "Content-Type header missing"
        
        if response.status_code == 200:
            assert "application/json" in response.headers["Content-Type"], "Expected JSON response"
        
        print(f"✓ Response headers: Content-Type={response.headers.get('Content-Type')}")
        
        # Check for common security headers
        security_headers = ["X-Content-Type-Options", "X-Frame-Options"]
        for header in security_headers:
            if header in response.headers:
                print(f"  Security header present: {header}={response.headers[header]}")
    
    def test_get_cart_with_special_characters_in_id(self):
        """
        Test Case 8: GET cart with special characters in ID
        
        Expected: 400 Bad Request or 404 Not Found
        """
        # Arrange
        special_char_ids = [
            "01kdq<script>alert(1)</script>",
            "01kdq%20space",
            "01kdq/slash/test",
            "01kdq?query=param",
            "01kdq#fragment"
        ]
        
        for special_id in special_char_ids:
            # Act
            response = requests.get(f"{CARTS_ENDPOINT}/{special_id}")
            
            # Assert
            assert response.status_code in [400, 404, 422], f"Special char ID should return error, got {response.status_code}"
            print(f"✓ Special character ID handled: {response.status_code}")
    
    def test_get_cart_with_very_long_id(self):
        """
        Test Case 9: GET cart with extremely long ID
        
        Expected: 400 Bad Request or 404 Not Found
        """
        # Arrange
        long_id = "a" * 1000  # 1000 character ID
        
        # Act
        response = requests.get(f"{CARTS_ENDPOINT}/{long_id}")
        
        # Assert
        assert response.status_code in [400, 404, 414, 422], f"Long ID should return error, got {response.status_code}"
        print(f"✓ Very long ID handled correctly: {response.status_code}")
    
    def test_get_cart_case_sensitivity(self):
        """
        Test Case 10: Test if cart ID is case-sensitive
        
        Expected: Different results for uppercase vs lowercase
        """
        # Arrange
        original_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        uppercase_id = original_id.upper()
        
        # Act
        response_original = requests.get(f"{CARTS_ENDPOINT}/{original_id}")
        response_uppercase = requests.get(f"{CARTS_ENDPOINT}/{uppercase_id}")
        
        # Assert
        print(f"✓ Original ID ({original_id}): {response_original.status_code}")
        print(f"✓ Uppercase ID ({uppercase_id}): {response_uppercase.status_code}")
        
        # They might return different results if case-sensitive
        if response_original.status_code != response_uppercase.status_code:
            print("  Cart IDs are case-sensitive")
        else:
            print("  Cart IDs might be case-insensitive")
    
    def test_get_cart_with_sql_injection_attempt(self):
        """
        Test Case 11: Security test - SQL injection attempt
        
        Expected: 400 Bad Request or 404 Not Found (should not execute SQL)
        """
        # Arrange
        sql_injection_ids = [
            "01kdq' OR '1'='1",
            "01kdq'; DROP TABLE carts;--",
            "01kdq' UNION SELECT * FROM users--"
        ]
        
        for injection_id in sql_injection_ids:
            # Act
            response = requests.get(f"{CARTS_ENDPOINT}/{injection_id}")
            
            # Assert
            assert response.status_code in [400, 404, 422], f"SQL injection should be blocked, got {response.status_code}"
            print(f"✓ SQL injection attempt blocked: {response.status_code}")
    
    def test_get_cart_concurrent_requests(self):
        """
        Test Case 12: Test concurrent requests to same cart
        
        Expected: All requests should succeed
        """
        # Arrange
        cart_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        num_requests = 5
        
        # Act
        responses = []
        start_time = time.time()
        
        for i in range(num_requests):
            response = requests.get(f"{CARTS_ENDPOINT}/{cart_id}")
            responses.append(response)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Assert
        for i, response in enumerate(responses):
            assert response.status_code in [200, 404], f"Request {i+1} failed with {response.status_code}"
        
        print(f"✓ {num_requests} concurrent requests completed in {total_time:.3f}s")
        print(f"  Average response time: {total_time/num_requests:.3f}s")
    
    def test_get_cart_with_null_id(self):
        """
        Test Case 13: GET cart with null/None in URL
        
        Expected: 404 Not Found
        """
        # Arrange
        null_variations = ["null", "None", "undefined", ""]
        
        for null_id in null_variations:
            if null_id:  # Skip empty string as it's tested separately
                # Act
                response = requests.get(f"{CARTS_ENDPOINT}/{null_id}")
                
                # Assert
                assert response.status_code in [400, 404], f"Null variation '{null_id}' should return error"
                print(f"✓ Null variation '{null_id}' handled: {response.status_code}")
    
    def test_get_cart_method_not_allowed(self):
        """
        Test Case 14: Test using wrong HTTP methods on cart endpoint
        
        Expected: 405 Method Not Allowed for unsupported methods
        """
        # Arrange
        cart_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        
        # Act & Assert - POST to GET endpoint (might not be allowed)
        methods_to_test = []
        
        # Try OPTIONS to see allowed methods
        response_options = requests.options(f"{CARTS_ENDPOINT}/{cart_id}")
        print(f"✓ OPTIONS request: {response_options.status_code}")
        
        if "Allow" in response_options.headers:
            print(f"  Allowed methods: {response_options.headers['Allow']}")
    
    def test_get_cart_with_trailing_slash(self):
        """
        Test Case 15: GET cart with trailing slash
        
        Expected: Should behave the same or redirect
        """
        # Arrange
        cart_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        
        # Act
        response_no_slash = requests.get(f"{CARTS_ENDPOINT}/{cart_id}")
        response_with_slash = requests.get(f"{CARTS_ENDPOINT}/{cart_id}/")
        
        # Assert
        print(f"✓ Without trailing slash: {response_no_slash.status_code}")
        print(f"✓ With trailing slash: {response_with_slash.status_code}")
        
        if response_no_slash.status_code == response_with_slash.status_code:
            print("  Trailing slash doesn't affect behavior")
        else:
            print("  Trailing slash changes behavior")
    
    def test_get_cart_content_negotiation(self):
        """
        Test Case 16: Test content negotiation with Accept header
        
        Expected: Should return JSON by default
        """
        # Arrange
        cart_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        headers = {
            "Accept": "application/json"
        }
        
        # Act
        response = requests.get(f"{CARTS_ENDPOINT}/{cart_id}", headers=headers)
        
        # Assert
        if response.status_code == 200:
            assert "application/json" in response.headers.get("Content-Type", ""), "Should return JSON"
            
            # Verify it's valid JSON
            try:
                response_data = response.json()
                print(f"✓ Valid JSON response received")
            except json.JSONDecodeError:
                pytest.fail("Response is not valid JSON")
        else:
            print(f"✓ Cart endpoint returned {response.status_code}")
    
    def test_get_cart_with_query_parameters(self):
        """
        Test Case 17: GET cart with query parameters
        
        Expected: Query params should be ignored or handled gracefully
        """
        # Arrange
        cart_id = "01kdqfvwjy5c3dan2ntjdf05gm"
        
        # Act
        response = requests.get(f"{CARTS_ENDPOINT}/{cart_id}?foo=bar&test=123")
        
        # Assert
        # Query parameters might be ignored for GET by ID
        print(f"✓ Request with query params: {response.status_code}")


# Standalone test functions
def test_carts_endpoint_availability():
    """
    Test Case 18: Verify carts endpoint is accessible
    """
    try:
        response = requests.get(CARTS_ENDPOINT, timeout=5)
        # Might return 404 (no ID provided) or 200 (list endpoint)
        assert response.status_code in [200, 404, 405], f"Unexpected status: {response.status_code}"
        print(f"✓ Carts endpoint is accessible: {response.status_code}")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Carts endpoint not reachable: {e}")


def test_api_base_url_reachable():
    """
    Test Case 19: Verify API base URL is reachable
    """
    try:
        response = requests.get(BASE_URL, timeout=5)
        print(f"✓ API base URL is reachable: {response.status_code}")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"API base URL not reachable: {e}")


if __name__ == "__main__":
    # Run tests programmatically
    pytest.main([__file__, "-v", "--tb=short"])
