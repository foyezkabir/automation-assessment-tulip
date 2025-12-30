from playwright.sync_api import Page, expect


class ContactPage:
    """Page Object Model for Contact Form"""
    
    def __init__(self, page: Page):
        self.page = page
        # Navigation
        self.nav_contact = page.locator("[data-test='nav-contact']")
        
        # Form fields
        self.first_name = page.locator("[data-test='first-name']")
        self.last_name = page.locator("[data-test='last-name']")
        self.email = page.locator("[data-test='email']")
        self.subject = page.locator("[data-test='subject']")
        self.message = page.locator("[data-test='message']")
        self.submit_button = page.locator("[data-test='contact-submit']")
        
    def goto(self):
        """Navigate to contact page"""
        self.page.goto("https://practicesoftwaretesting.com/")
        self.nav_contact.click()
    
    def submit_empty_form(self):
        """Submit form without filling any fields"""
        self.submit_button.click()
    
    def verify_required_errors(self):
        """Verify all required field error messages"""
        expect(self.page.get_by_text("First name is required")).to_be_visible()
        expect(self.page.get_by_text("Last name is required")).to_be_visible()
        expect(self.page.get_by_text("Email is required")).to_be_visible()
        expect(self.page.get_by_text("Subject is required")).to_be_visible()
        expect(self.page.get_by_text("Message is required")).to_be_visible()
    
    def fill_contact_form(self, first_name: str, last_name: str, email: str, 
                          subject: str, message: str):
        """Fill all contact form fields"""
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.email.fill(email)
        self.subject.select_option(subject)
        self.message.fill(message)
    
    def submit_form(self):
        """Submit the contact form"""
        self.submit_button.click()
    
    def verify_success_message(self):
        """Verify form submission success"""
        expect(self.page.get_by_text("Thanks for your message! We")).to_be_visible()


# Test cases
def test_contact_form_validation(page: Page) -> None:
    """Test contact form validation errors"""
    contact = ContactPage(page)
    contact.goto()
    contact.submit_empty_form()
    contact.verify_required_errors()


def test_contact_form_submission(page: Page) -> None:
    """Test successful contact form submission"""
    contact = ContactPage(page)
    contact.goto()
    contact.fill_contact_form(
        first_name="Foyez",
        last_name="Kabir",
        email="foyezkabir00@gmail.com",
        subject="webmaster",
        message="This is a dummy text, Please do not reply to this one"
    )
    contact.submit_form()
    contact.verify_success_message()
