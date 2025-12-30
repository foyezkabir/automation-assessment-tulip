from playwright.sync_api import Page


class cartLoc:
    """Locators for Product and Cart Pages"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Product page elements
        self.product_title = page.locator("h1")
        self.product_price = page.locator(".card-title").filter(has_text="$")
        self.quantity_input = page.locator("[data-test='quantity']")
        self.increase_quantity_btn = page.locator("[data-test='increase-quantity']")
        self.decrease_quantity_btn = page.locator("[data-test='decrease-quantity']")
        self.add_to_cart_btn = page.locator("[data-test='add-to-cart']")
        
        # Cart page elements
        self.nav_cart = page.locator("[data-test='nav-cart']")
        self.cart_badge = page.locator(".badge")
        self.cart_product_title = page.locator("[data-test='product-title']")
        self.cart_product_quantity = page.locator("[data-test='product-quantity']")
        self.cart_product_price = page.locator("[data-test='product-price']")
        self.cart_total = page.locator("[data-test='cart-total']")
        self.proceed_btn = page.locator("[data-test='proceed-1']")
        self.continue_shopping_btn = page.locator("[data-test='continue-shopping']")
