import pytest
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import Page
from Pages.cartPage import CartPage


@pytest.fixture
def cart(page: Page):
    """
    Fixture to provide CartPage instance
    """
    cart_page = CartPage(page)
    return cart_page


def test_add_to_cart_and_verify(cart: CartPage):
    """
    Test Case 1: Add product to cart, verify, then add multiple quantity
    
    Steps:
    1. Navigate to Combination Pliers product page
    2. Add product to cart
    3. Verify cart badge shows 1 item
    4. Navigate to cart page
    5. Verify product appears in cart with correct details
    6. Go back to product page and add 2 more items
    7. Verify cart shows updated quantity (3 items) and total price
    """
    # Arrange
    expected_product = "Combination Pliers"
    initial_price = "$14.15"
    
    # Act - Add first item
    cart.goto_combination_pliers()
    cart.click_add_to_cart()
    
    # Assert - Verify cart badge
    cart.expect_cart_badge_count("1")
    
    # Act - Navigate to cart
    cart.click_nav_cart()
    time.sleep(3)  # Wait for navigation
    
    # Assert - Verify product in cart
    cart.expect_cart_product_title(expected_product)
    cart.expect_cart_product_quantity("1")
    cart.expect_cart_product_price(initial_price)
    cart.expect_cart_total(initial_price)
    
    # Act - Go back and add multiple quantity (2 more items)
    cart.goto_combination_pliers()
    cart.fill_quantity("2")
    cart.click_add_to_cart()
    time.sleep(1)  # Wait for cart update
    
    # Assert - Cart badge should now show 3 items (1 + 2)
    cart.expect_cart_badge_count("3")
    
    # Act - Navigate to cart again
    cart.click_nav_cart()
    time.sleep(1)  # Wait for navigation
    
    # Assert - Verify updated quantity and total
    cart.expect_cart_product_quantity("3")
    cart.expect_cart_product_price(initial_price)
    cart.expect_cart_total("$42.45")  # 3 × $14.15 = $42.45
    time.sleep(2)  # Pause to observe final state