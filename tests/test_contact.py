import pytest
import time
from playwright.sync_api import Page
from contactPage import ContactPage


@pytest.fixture
def contact(page: Page):
    """
    Fixture to automatically navigate to contact form before test execution
    """
    contact_page = ContactPage(page)
    contact_page.goto()
    contact_page.click_nav_contact()
    return contact_page


def test_contact_form_validation_empty_fields(contact: ContactPage):
    """
    Test Case 1: Verify validation errors on empty form submission
    """
    # Act
    contact.click_submit()
    time.sleep(1)  # Wait for error messages to appear
    contact.page.evaluate("window.scrollTo(0, 0)")  # Scroll to top to see first name and last name fields
    time.sleep(1)
    
    # Assert
    contact.verify_all_required_errors()


def test_contact_form_successful_submission(contact: ContactPage):
    """
    Test Case 2: Verify successful form submission with valid data
    """
    # Arrange
    test_data = {
        "first_name": "Foyez",
        "last_name": "Kabir",
        "email": "foyezkabir00@gmail.com",
        "subject": "webmaster",
        "message": "This is a test message for automation testing. do not reply to this email. just ignore it."
    }
    
    # Act
    contact.fill_complete_form(**test_data)
    contact.click_submit()
    
    # Assert
    contact.expect_success_message()


def test_contact_form_validation_and_correction(contact: ContactPage):
    """
    Test Case 3: Verify validation errors can be corrected
    """
    # Act - Submit empty and verify errors
    contact.click_submit()
    contact.verify_all_required_errors()
    
    # Act - Fill and submit
    contact.fill_complete_form(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        subject="Return",
        message="Test message after validation.Test message after validation.Test message after validation.Test message after validation. "
    )
    contact.click_submit()
    
    # Assert
    contact.expect_success_message()

