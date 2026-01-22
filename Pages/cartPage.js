const { expect } = require('@playwright/test');
const { CartLocators } = require('../Locators/cartLoc');

class CartPage {
    /**
     * Page Object Model for Product and Cart Pages with granular actions
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this._locators = new CartLocators(page);
    }

    // Navigation actions
    async gotoHome() {
        await this.page.goto('https://practicesoftwaretesting.com/');
    }

    async gotoProduct(productUrl) {
        await this.page.goto(productUrl);
    }

    async gotoCombinationPliers() {
        await this.gotoHome();
        // Click on the Combination Pliers product link from homepage
        await this.page.getByRole('link', { name: 'Combination Pliers Combination' }).click();
        await this._locators.addToCartBtn.waitFor({ state: 'visible', timeout: 10000 });
    }

    async clickNavCart() {
        await this._locators.navCart.click();
    }

    async gotoCart() {
        await this.page.goto('https://practicesoftwaretesting.com/checkout');
        await this._locators.cartProductTitle.waitFor({ state: 'visible', timeout: 10000 });
    }

    // Product page actions
    async getProductTitle() {
        return await this._locators.productTitle.textContent();
    }

    async getProductPrice() {
        return await this._locators.productPrice.textContent();
    }

    async clickQuantityInput() {
        await this._locators.quantityInput.click();
    }

    async fillQuantity(value) {
        await this._locators.quantityInput.fill(value);
    }

    async clickIncreaseQuantity() {
        await this._locators.increaseQuantityBtn.click();
    }

    async clickDecreaseQuantity() {
        await this._locators.decreaseQuantityBtn.click();
    }

    async clickAddToCart() {
        await this._locators.addToCartBtn.click();
        // Cart badge will auto-update, no explicit wait needed
    }

    async expectAddToCartVisible() {
        await expect(this._locators.addToCartBtn).toBeVisible();
    }

    // Cart page actions
    async getCartBadgeCount() {
        return await this._locators.cartBadge.textContent();
    }

    async expectCartBadgeCount(expectedCount) {
        await expect(this._locators.cartBadge).toHaveText(expectedCount);
    }

    async getCartProductTitle() {
        return await this._locators.cartProductTitle.textContent();
    }

    async expectCartProductTitle(expectedTitle) {
        await expect(this._locators.cartProductTitle).toContainText(expectedTitle);
    }

    async getCartProductQuantity() {
        return await this._locators.cartProductQuantity.inputValue();
    }

    async fillCartProductQuantity(value) {
        await this._locators.cartProductQuantity.fill(value);
        await this.page.keyboard.press('Tab'); // Trigger update
        await this.page.waitForTimeout(2000); // Wait for price calculation
    }

    async expectCartProductQuantity(expectedQuantity) {
        await expect(this._locators.cartProductQuantity).toHaveValue(expectedQuantity);
    }

    async getCartProductPrice() {
        return await this._locators.cartProductPrice.textContent();
    }

    async expectCartProductPrice(expectedPrice) {
        await expect(this._locators.cartProductPrice).toHaveText(expectedPrice);
    }

    async getCartTotal() {
        return await this._locators.cartTotal.textContent();
    }

    async expectCartTotal(expectedTotal) {
        await expect(this._locators.cartTotal).toHaveText(expectedTotal);
    }

    async clickProceed() {
        await this._locators.proceedBtn.click();
    }

    async clickContinueShopping() {
        await this._locators.continueShoppingBtn.click();
    }

    // Combined convenience methods
    async addProductToCartWithQuantity(quantity = 1) {
        if (quantity > 1) {
            await this.fillQuantity(quantity.toString());
        }
        await this.clickAddToCart();
    }

    async verifyProductInCart(productName, quantity, unitPrice, totalPrice) {
        await this.expectCartProductTitle(productName);
        await this.expectCartProductQuantity(quantity);
        await this.expectCartProductPrice(unitPrice);
        await this.expectCartTotal(totalPrice);
    }

    async updateCartQuantityAndVerify(newQuantity, expectedTotal) {
        await this.fillCartProductQuantity(newQuantity);
        await this.expectCartProductQuantity(newQuantity);
        await this.expectCartTotal(expectedTotal);
    }
}

module.exports = { CartPage };
