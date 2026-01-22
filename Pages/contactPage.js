const { expect } = require('@playwright/test');
const { ContactLocators } = require('../Locators/contactLoc');

class ContactPage {
    /**
     * Page Object Model for Contact Form with granular actions
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;

        // Initialize locators
        const locators = new ContactLocators(page);

        // Navigation
        this.navContact = locators.navContact;

        // Form fields
        this.firstName = locators.firstName;
        this.lastName = locators.lastName;
        this.email = locators.email;
        this.subject = locators.subject;
        this.message = locators.message;
        this.submitButton = locators.submitButton;
    }

    // Navigation actions
    async goto() {
        await this.page.goto('https://practicesoftwaretesting.com/');
    }

    async clickNavContact() {
        await this.navContact.click();
    }

    // First Name actions
    async clickFirstName() {
        await this.firstName.click();
    }

    async fillFirstName(value) {
        await this.firstName.fill(value);
    }

    async expectFirstNameVisible() {
        await expect(this.firstName).toBeVisible();
    }

    async expectFirstNameError() {
        await expect(this.page.getByText('First name is required')).toBeVisible();
    }

    // Last Name actions
    async clickLastName() {
        await this.lastName.click();
    }

    async fillLastName(value) {
        await this.lastName.fill(value);
    }

    async expectLastNameVisible() {
        await expect(this.lastName).toBeVisible();
    }

    async expectLastNameError() {
        await expect(this.page.getByText('Last name is required')).toBeVisible();
    }

    // Email actions
    async clickEmail() {
        await this.email.click();
    }

    async fillEmail(value) {
        await this.email.fill(value);
    }

    async expectEmailVisible() {
        await expect(this.email).toBeVisible();
    }

    async expectEmailError() {
        await expect(this.page.getByText('Email is required')).toBeVisible();
    }

    // Subject actions
    async clickSubject() {
        await this.subject.click();
    }

    async selectSubject(value) {
        await this.subject.selectOption(value);
    }

    async expectSubjectVisible() {
        await expect(this.subject).toBeVisible();
    }

    async expectSubjectError() {
        await expect(this.page.getByText('Subject is required')).toBeVisible();
    }

    // Message actions
    async clickMessage() {
        await this.message.click();
    }

    async fillMessage(value) {
        await this.message.fill(value);
    }

    async expectMessageVisible() {
        await expect(this.message).toBeVisible();
    }

    async expectMessageError() {
        await expect(this.page.getByText('Message is required')).toBeVisible();
    }

    // Submit button actions
    async clickSubmit() {
        await this.submitButton.click();
    }

    async expectSubmitVisible() {
        await expect(this.submitButton).toBeVisible();
    }

    // Success message
    async expectSuccessMessage() {
        await expect(this.page.getByText('Thanks for your message! We')).toBeVisible();
    }

    // Combined actions for convenience
    async submitEmptyForm() {
        await this.clickSubmit();
    }

    async verifyAllRequiredErrors() {
        await this.expectFirstNameError();
        await this.expectLastNameError();
        await this.expectEmailError();
        await this.expectSubjectError();
        await this.expectMessageError();
    }

    async fillCompleteForm({ firstName, lastName, email, subject, message }) {
        await this.fillFirstName(firstName);
        await this.fillLastName(lastName);
        await this.fillEmail(email);
        await this.selectSubject(subject);
        await this.fillMessage(message);
    }
}

module.exports = { ContactPage };
