class ContactLocators {
    /**
     * Locators for Contact Form Page
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;

        // Navigation
        this.navContact = page.locator("[data-test='nav-contact']");

        // Form fields
        this.firstName = page.locator("[data-test='first-name']");
        this.lastName = page.locator("[data-test='last-name']");
        this.email = page.locator("[data-test='email']");
        this.subject = page.locator("[data-test='subject']");
        this.message = page.locator("[data-test='message']");
        this.submitButton = page.locator("[data-test='contact-submit']");
    }
}

module.exports = { ContactLocators };
