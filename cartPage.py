from playwright.sync_api import Page, expect
import time
from cartLoc import cartLoc


class CartPage:
    """Page Object Model for Product and Cart Pages with granular actions"""
    
    def __init__(self, page: Page):
        self.page = page
        self._locators = cartLoc(page)
    
    # Navigation actions
    def goto_home(self):
        """Navigate to home page"""
        self.page.goto("https://practicesoftwaretesting.com/")
    
    def goto_product(self, product_url: str):
        """Navigate to specific product page"""
        self.page.goto(product_url)
    
    def goto_combination_pliers(self):
        """Navigate to Combination Pliers product page"""
        self.goto_home()
        # Click on the Combination Pliers product link from homepage
        self.page.get_by_role("link", name="Combination Pliers Combination").click()
        self._locators.add_to_cart_btn.wait_for(state="visible", timeout=10000)
    
    def click_nav_cart(self):
        """Click cart navigation icon"""
        self._locators.nav_cart.click()
    
    def goto_cart(self):
        """Navigate to cart/checkout page"""
        self.page.goto("https://practicesoftwaretesting.com/checkout")
        self._locators.cart_product_title.wait_for(state="visible", timeout=10000)
    
    # Product page actions
    def get_product_title(self) -> str:
        """Get product title text"""
        return self._locators.product_title.text_content()
    
    def get_product_price(self) -> str:
        """Get product price text"""
        return self._locators.product_price.text_content()
    
    def click_quantity_input(self):
        """Click quantity input field"""
        self._locators.quantity_input.click()
    
    def fill_quantity(self, value: str):
        """Fill quantity input field"""
        self._locators.quantity_input.fill(value)
    
    def click_increase_quantity(self):
        """Click increase quantity button"""
        self._locators.increase_quantity_btn.click()
    
    def click_decrease_quantity(self):
        """Click decrease quantity button"""
        self._locators.decrease_quantity_btn.click()
    
    def click_add_to_cart(self):
        """Click add to cart button"""
        self._locators.add_to_cart_btn.click()
        time.sleep(1)  # Wait for cart update
    
    def expect_add_to_cart_visible(self):
        """Verify add to cart button is visible"""
        expect(self._locators.add_to_cart_btn).to_be_visible()
    
    # Cart page actions
    def get_cart_badge_count(self) -> str:
        """Get cart badge count"""
        return self._locators.cart_badge.text_content()
    
    def expect_cart_badge_count(self, expected_count: str):
        """Verify cart badge shows expected count"""
        expect(self._locators.cart_badge).to_have_text(expected_count)
    
    def get_cart_product_title(self) -> str:
        """Get product title in cart"""
        return self._locators.cart_product_title.text_content()
    
    def expect_cart_product_title(self, expected_title: str):
        """Verify product title in cart"""
        expect(self._locators.cart_product_title).to_contain_text(expected_title)
    
    def get_cart_product_quantity(self) -> str:
        """Get product quantity in cart"""
        return self._locators.cart_product_quantity.input_value()
    
    def fill_cart_product_quantity(self, value: str):
        """Update product quantity in cart"""
        self._locators.cart_product_quantity.fill(value)
        self.page.keyboard.press("Tab")  # Trigger update
        time.sleep(2)  # Wait for price calculation
    
    def expect_cart_product_quantity(self, expected_quantity: str):
        """Verify product quantity in cart"""
        expect(self._locators.cart_product_quantity).to_have_value(expected_quantity)
    
    def get_cart_product_price(self) -> str:
        """Get product unit price in cart"""
        return self._locators.cart_product_price.text_content()
    
    def expect_cart_product_price(self, expected_price: str):
        """Verify product unit price in cart"""
        expect(self._locators.cart_product_price).to_have_text(expected_price)
    
    def get_cart_total(self) -> str:
        """Get cart total price"""
        return self._locators.cart_total.text_content()
    
    def expect_cart_total(self, expected_total: str):
        """Verify cart total price"""
        expect(self._locators.cart_total).to_have_text(expected_total)
    
    def click_proceed(self):
        """Click proceed to checkout button"""
        self._locators.proceed_btn.click()
    
    def click_continue_shopping(self):
        """Click continue shopping button"""
        self._locators.continue_shopping_btn.click()
    
    # Combined convenience methods
    def add_product_to_cart_with_quantity(self, quantity: int = 1):
        """Add product to cart with specified quantity"""
        if quantity > 1:
            self.fill_quantity(str(quantity))
        self.click_add_to_cart()
    
    def verify_product_in_cart(self, product_name: str, quantity: str, unit_price: str, total_price: str):
        """Verify product details in cart"""
        self.expect_cart_product_title(product_name)
        self.expect_cart_product_quantity(quantity)
        self.expect_cart_product_price(unit_price)
        self.expect_cart_total(total_price)
    
    def update_cart_quantity_and_verify(self, new_quantity: str, expected_total: str):
        """Update cart quantity and verify total price updates"""
        self.fill_cart_product_quantity(new_quantity)
        self.expect_cart_product_quantity(new_quantity)
        self.expect_cart_total(expected_total)
