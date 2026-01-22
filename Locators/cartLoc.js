const { expect } = require('@playwright/test');

class CartLocators {
    /**
     * Locators for Product and Cart Pages
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;

        // Product page elements
        this.productTitle = page.locator('h1');
        this.productPrice = page.locator('.card-title').filter({ hasText: '$' });
        this.quantityInput = page.locator("[data-test='quantity']");
        this.increaseQuantityBtn = page.locator("[data-test='increase-quantity']");
        this.decreaseQuantityBtn = page.locator("[data-test='decrease-quantity']");
        this.addToCartBtn = page.locator("[data-test='add-to-cart']");

        // Cart page elements
        this.navCart = page.locator("[data-test='nav-cart']");
        this.cartBadge = page.locator("[data-test='nav-cart'] .badge");
        this.cartProductTitle = page.locator("[data-test='product-title']");
        this.cartProductQuantity = page.locator("[data-test='product-quantity']");
        this.cartProductPrice = page.locator("[data-test='product-price']");
        this.cartTotal = page.locator("[data-test='cart-total']");
        this.proceedBtn = page.locator("[data-test='proceed-1']");
        this.continueShoppingBtn = page.locator("[data-test='continue-shopping']");
    }
}

module.exports = { CartLocators };
