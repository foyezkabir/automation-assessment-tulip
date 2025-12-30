from playwright.sync_api import Page, expect


class ContactPage:
    """Page Object Model for Contact Form with granular actions"""
    
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
    
    # Navigation actions
    def goto(self):
        """Navigate to contact page"""
        self.page.goto("https://practicesoftwaretesting.com/")
    
    def click_nav_contact(self):
        """Click contact navigation link"""
        self.nav_contact.click()
    
    # First Name actions
    def click_first_name(self):
        """Click first name field"""
        self.first_name.click()
    
    def fill_first_name(self, value: str):
        """Fill first name field"""
        self.first_name.fill(value)
    
    def expect_first_name_visible(self):
        """Verify first name field is visible"""
        expect(self.first_name).to_be_visible()
    
    def expect_first_name_error(self):
        """Verify first name required error"""
        expect(self.page.get_by_text("First name is required")).to_be_visible()
    
    # Last Name actions
    def click_last_name(self):
        """Click last name field"""
        self.last_name.click()
    
    def fill_last_name(self, value: str):
        """Fill last name field"""
        self.last_name.fill(value)
    
    def expect_last_name_visible(self):
        """Verify last name field is visible"""
        expect(self.last_name).to_be_visible()
    
    def expect_last_name_error(self):
        """Verify last name required error"""
        expect(self.page.get_by_text("Last name is required")).to_be_visible()
    
    # Email actions
    def click_email(self):
        """Click email field"""
        self.email.click()
    
    def fill_email(self, value: str):
        """Fill email field"""
        self.email.fill(value)
    
    def expect_email_visible(self):
        """Verify email field is visible"""
        expect(self.email).to_be_visible()
    
    def expect_email_error(self):
        """Verify email required error"""
        expect(self.page.get_by_text("Email is required")).to_be_visible()
    
    # Subject actions
    def click_subject(self):
        """Click subject dropdown"""
        self.subject.click()
    
    def select_subject(self, value: str):
        """Select subject option"""
        self.subject.select_option(value)
    
    def expect_subject_visible(self):
        """Verify subject field is visible"""
        expect(self.subject).to_be_visible()
    
    def expect_subject_error(self):
        """Verify subject required error"""
        expect(self.page.get_by_text("Subject is required")).to_be_visible()
    
    # Message actions
    def click_message(self):
        """Click message field"""
        self.message.click()
    
    def fill_message(self, value: str):
        """Fill message field"""
        self.message.fill(value)
    
    def expect_message_visible(self):
        """Verify message field is visible"""
        expect(self.message).to_be_visible()
    
    def expect_message_error(self):
        """Verify message required error"""
        expect(self.page.get_by_text("Message is required")).to_be_visible()
    
    # Submit button actions
    def click_submit(self):
        """Click submit button"""
        self.submit_button.click()
    
    def expect_submit_visible(self):
        """Verify submit button is visible"""
        expect(self.submit_button).to_be_visible()
    
    # Success message
    def expect_success_message(self):
        """Verify form submission success"""
        expect(self.page.get_by_text("Thanks for your message! We")).to_be_visible()
    
    # Combined actions for convenience
    def submit_empty_form(self):
        """Submit form without filling any fields"""
        self.click_submit()
    
    def verify_all_required_errors(self):
        """Verify all required field error messages"""
        self.expect_first_name_error()
        self.expect_last_name_error()
        self.expect_email_error()
        self.expect_subject_error()
        self.expect_message_error()
    
    def fill_complete_form(self, first_name: str, last_name: str, email: str, 
                          subject: str, message: str):
        """Fill all contact form fields"""
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.select_subject(subject)
        self.fill_message(message)
