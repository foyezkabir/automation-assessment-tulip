import pytest
import time
from playwright.sync_api import Page
from cartPage import CartPage


@pytest.fixture
def cart(page: Page):
    """
    Fixture to provide CartPage instance
    """
    cart_page = CartPage(page)
    return cart_page


def test_add_to_cart_and_verify(cart: CartPage):
    """
    Test Case 1: Add product to cart and verify it appears
    
    Steps:
    1. Navigate to Combination Pliers product page
    2. Add product to cart
    3. Verify cart badge shows 1 item
    4. Navigate to cart page
    5. Verify product appears in cart with correct details
    """
    # Arrange
    expected_product = "Combination Pliers"
    expected_price = "$14.15"
    
    # Act
    cart.goto_combination_pliers()
    cart.click_add_to_cart()
    
    # Assert - Verify cart badge
    cart.expect_cart_badge_count("1")
    
    # Act - Navigate to cart
    cart.goto_cart()
    
    # Assert - Verify product in cart
    cart.expect_cart_product_title(expected_product)
    cart.expect_cart_product_quantity("1")
    cart.expect_cart_product_price(expected_price)
    cart.expect_cart_total(expected_price)


def test_update_cart_quantity_and_verify_price(cart: CartPage):
    """
    Test Case 2: Update cart quantity and verify price updates
    
    Steps:
    1. Navigate to Combination Pliers product page
    2. Add product to cart
    3. Navigate to cart page
    4. Update quantity to 3
    5. Verify total price is updated correctly (3 × $14.15 = $42.45)
    """
    # Arrange
    initial_price = "$14.15"
    new_quantity = "3"
    expected_total = "$42.45"
    
    # Act - Add to cart
    cart.goto_combination_pliers()
    cart.click_add_to_cart()
    cart.goto_cart()
    
    # Assert - Verify initial state
    cart.expect_cart_product_quantity("1")
    cart.expect_cart_total(initial_price)
    
    # Act - Update quantity
    cart.update_cart_quantity_and_verify(new_quantity, expected_total)


def test_add_multiple_quantity_to_cart(cart: CartPage):
    """
    Test Case 3: Add product with quantity > 1 directly
    
    Steps:
    1. Navigate to Combination Pliers product page
    2. Set quantity to 2 before adding to cart
    3. Add to cart
    4. Verify cart shows 2 items
    5. Navigate to cart and verify quantity and price
    """
    # Arrange
    quantity = "2"
    unit_price = "$14.15"
    expected_total = "$28.30"  # 2 × 14.15
    
    # Act
    cart.goto_combination_pliers()
    cart.fill_quantity(quantity)
    cart.click_add_to_cart()
    
    # Assert - Cart badge shows quantity
    cart.expect_cart_badge_count("2")
    
    # Act - Navigate to cart
    cart.goto_cart()
    
    # Assert - Verify details
    cart.expect_cart_product_quantity(quantity)
    cart.expect_cart_product_price(unit_price)
    cart.expect_cart_total(expected_total)
