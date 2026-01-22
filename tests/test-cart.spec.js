const { test, expect } = require('@playwright/test');
const { CartPage } = require('../Pages/cartPage');

/**
 * Test suite for Cart functionality
 */

test.describe('Cart Tests', () => {
    let cartPage;

    test.beforeEach(async ({ page }) => {
        // Setup: Create CartPage instance
        cartPage = new CartPage(page);
    });

    test('Test Case 1: Add product to cart, verify, then add multiple quantity', async ({ page }) => {
        /**
         * Steps:
         * 1. Navigate to Combination Pliers product page
         * 2. Add product to cart
         * 3. Verify cart badge shows 1 item
         * 4. Navigate to cart page
         * 5. Verify product appears in cart with correct details
         * 6. Go back to product page and add 2 more items
         * 7. Verify cart shows updated quantity (3 items) and total price
         */

        // Arrange
        const expectedProduct = 'Combination Pliers';
        const initialPrice = '$14.15';

        // Act - Add first item
        await cartPage.gotoCombinationPliers();
        await cartPage.clickAddToCart();

        // Assert - Verify cart badge
        await cartPage.expectCartBadgeCount('1');

        // Act - Navigate to cart
        await cartPage.clickNavCart();
        await page.waitForURL('**/checkout');

        // Assert - Verify product in cart
        await cartPage.expectCartProductTitle(expectedProduct);
        await cartPage.expectCartProductQuantity('1');
        await cartPage.expectCartProductPrice(initialPrice);
        await cartPage.expectCartTotal(initialPrice);

        // Act - Go back and add multiple quantity (2 more items)
        await cartPage.gotoCombinationPliers();
        await cartPage.fillQuantity('2');
        await cartPage.clickAddToCart();

        // Assert - Cart badge should now show 3 items (1 + 2)
        await cartPage.expectCartBadgeCount('3');

        // Act - Navigate to cart again
        await cartPage.clickNavCart();
        await page.waitForURL('**/checkout');

        // Assert - Verify updated quantity and total
        await cartPage.expectCartProductQuantity('3');
        await cartPage.expectCartProductPrice(initialPrice);
        await cartPage.expectCartTotal('$42.45'); // 3 × $14.15 = $42.45
    });
});
