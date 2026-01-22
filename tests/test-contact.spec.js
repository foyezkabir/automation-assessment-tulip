const { test, expect } = require('@playwright/test');
const { ContactPage } = require('../Pages/contactPage');

/**
 * Test suite for Contact Form
 */

test.describe('Contact Form Tests', () => {
    let contactPage;

    test.beforeEach(async ({ page }) => {
        // Setup: Navigate to contact form before each test
        contactPage = new ContactPage(page);
        await contactPage.goto();
        await contactPage.clickNavContact();
    });

    test('Test Case 1: Verify validation errors on empty form submission', async ({ page }) => {
        // Act
        await contactPage.clickSubmit();
        await page.evaluate(() => window.scrollTo(0, 0)); // Scroll to top to see first name and last name fields

        // Assert
        await contactPage.verifyAllRequiredErrors();
    });

    test('Test Case 2: Verify successful form submission with valid data', async () => {
        // Arrange
        const testData = {
            firstName: 'Foyez',
            lastName: 'Kabir',
            email: 'foyezkabir00@gmail.com',
            subject: 'webmaster',
            message: 'This is a test message for automation testing. do not reply to this email. just ignore it.'
        };

        // Act
        await contactPage.fillCompleteForm(testData);
        await contactPage.clickSubmit();

        // Assert
        await contactPage.expectSuccessMessage();
    });

    test('Test Case 3: Verify validation errors can be corrected', async () => {
        // Act - Submit empty and verify errors
        await contactPage.clickSubmit();
        await contactPage.verifyAllRequiredErrors();

        // Act - Fill and submit
        await contactPage.fillCompleteForm({
            firstName: 'John',
            lastName: 'Doe',
            email: 'john.doe@example.com',
            subject: 'Return',
            message: 'Test message after validation.Test message after validation.Test message after validation.Test message after validation. '
        });
        await contactPage.clickSubmit();

        // Assert
        await contactPage.expectSuccessMessage();
    });
});
