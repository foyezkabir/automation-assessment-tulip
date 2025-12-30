# Automation Assessment Project

A comprehensive test automation framework using Playwright and Selenium with Python for web application testing, featuring authentication state management and Page Object Model pattern.

## 🎯 Project Overview

This project demonstrates automated testing capabilities for two web applications:
1. **Practice Software Testing** (https://practicesoftwaretesting.com/) - E-commerce testing

## 🏗️ Architecture

```
automation-assessment/
├── .github/
│   └── copilot-instructions.md    # AI agent guidelines
├── Locators/                       # Element locator classes
│   ├── cartLoc.py                 # Cart & product page locators
│   └── contactLoc.py              # Contact form locators
├── Pages/                          # Page Object Models
│   ├── cartPage.py                # Cart & product page actions
│   └── contactPage.py             # Contact form page actions
├── tests/                          # Test files
│   ├── test_cart.py               # Cart functionality tests
│   └── test_contact.py            # Contact form tests
├── auth_helper.py                  # Authentication utilities
├── auth_state.json                 # Cached JWT tokens
├── conftest.py                     # pytest configuration
├── test_api.py                     # API tests for messages endpoint
├── test_login_playwright.py        # Login & storage state tests
├── test_playwright.py              # Basic Playwright tests
├── test_selenium.py                # Basic Selenium tests
└── requirements.txt                # Python dependencies
```

## 🚀 Features

### 1. **Page Object Model (POM) Pattern**
- Two-layer architecture: Locators (in `Locators/`) + Page Objects (in `Pages/`)
- Granular action methods for each UI element
- Combined convenience methods for complex workflows
- Proper module imports using `sys.path` configuration

### 2. **Authentication State Management**
- Single login with JWT token caching
- Reusable authentication across tests
- Storage state persists: id_token, access_token, refresh_token
- No repeated login overhead

### 3. **Test Categories**

#### Contact Form Tests (`tests/test_contact.py`)
- ✅ Empty form validation
- ✅ Successful submission with valid data
- ✅ Error correction workflow

#### Cart Functionality Tests (`tests/test_cart.py`)
- ✅ Add product to cart and verify
- ✅ Update cart quantity (1 → 3)
- ✅ Add multiple quantities directly
- ✅ Price calculation verification

#### API Tests (`test_api.py`)
- ✅ POST message with valid data
- ✅ Validation tests for missing fields
- ✅ Invalid email format handling
- ✅ Special characters support
- ✅ Response time verification
- ✅ Response headers validation

## 📦 Installation

### Prerequisites
- Python 3.12+
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/foyezkabir/automation-assessment-tulip.git
cd automation-assessment-tulip
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers**
```bash
playwright install chromium
```

## 🧪 Running Tests

### Run All Tests
```bash
python -m pytest -v
```

### Run Specific Test Files
```bash
# Contact form tests
python -m pytest tests/test_contact.py -v

# Cart functionality tests
python -m pytest tests/test_cart.py -v

# API tests
python -m pytest test_api.py -v
```

### Run Individual Test
```bash
python -m pytest tests/test_contact.py::test_contact_form_validation_empty_fields -v
python -m pytest tests/test_cart.py::test_add_to_cart_and_verify -v
python -m pytest test_api.py::TestMessagesAPI::test_post_message_success -v
```

## 🔧 Configuration

### Browser Settings (`conftest.py`)
```python
# Headed mode with slow motion for visibility
"headless": False
"slow_mo": 500  # 500ms delay between actions
```

### Authentication Credentials
- Email: `r8ete3@onemail.host`
- Password: `Kabir123#`
- Storage: `auth_state.json`

## 📝 Test Patterns

### Fixture-Based Setup
```python
# tests/test_contact.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.contactPage import ContactPage

@pytest.fixture
def contact(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()
    contact_page.click_nav_contact()
    return contact_page
```

### AAA (Arrange-Act-Assert) Pattern
```python
def test_add_to_cart_and_verify(cart: CartPage):
    # Arrange
    expected_product = "Combination Pliers"
    expected_price = "$14.15"
    
    # Act
    cart.goto_combination_pliers()
    cart.click_add_to_cart()
    
    # Assert
    cart.expect_cart_badge_count("1")
```

## 🎨 Code Conventions

### Locator Strategy
1. **Primary**: `data-test` attributes
   ```python
   page.locator("[data-test='add-to-cart']")
   ```

2. **Specific selectors**: Combine selectors for uniqueness
   ```python
   # Cart badge - specific to navigation cart icon
   page.locator("[data-test='nav-cart'] .badge")
   ```

3. **Auth forms**: `get_by_role()` for accessibility
   ```python
   page.get_by_role("textbox", name="Email")
   ```

4. **Validation messages**: `get_by_text()` for exact matching
   ```python
   page.get_by_text("First name is required")
   ```

### Import Pattern
```python
# Page Objects import locators from Locators folder
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Locators.cartLoc import cartLoc

# Test files import from Pages folder
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.cartPage import CartPage
```

## 📊 Test Results

### Cart Tests (`tests/test_cart.py`)
- ✅ `test_add_to_cart_and_verify` - Verifies product appears in cart
- ✅ `test_update_cart_quantity_and_verify_price` - Updates quantity: 1→3, price: $14.15→$42.45
- ✅ `test_add_multiple_quantity_to_cart` - Adds 2 items, verifies total: $28.30

### Contact Form Tests (`tests/test_contact.py`)
- ✅ `test_contact_form_validation_empty_fields` - All 5 required field errors shown
- ✅ `test_contact_form_successful_submission` - Success message displayed
- ✅ `test_contact_form_validation_and_correction` - Error → Fix → Success flow

### API Tests (`test_api.py`)
- ✅ `test_post_message_success` - POST message with all fields returns 200 OK
- ✅ `test_post_message_missing_name` - Handles missing name field
- ✅ `test_post_message_invalid_email_format` - Validates email format (422)
- ✅ `test_post_message_response_time` - Response < 3 seconds
- ✅ `test_post_message_special_characters` - Handles special characters correctly

## 🛠️ Technologies Used

- **Playwright** 1.57.0 - Modern browser automation
- **Selenium** 4.39.0 - Cross-browser testing
- **pytest** 9.0.2 - Test framework
- **pytest-playwright** 0.7.2 - Playwright-pytest integration
- **requests** 2.32.5 - API testing
- **webdriver-manager** 4.0.2 - Automatic driver management

## 🐛 Debugging

### View Test Execution
Tests run in **headed mode** with 500ms slow motion by default for visibility.

### Common Issues

**Import Errors**
```bash
# Solution: Use sys.path to add parent directory
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

**Locator Ambiguity**
```bash
# Solution: Make locators more specific
# Bad: page.locator(".badge")  # Matches multiple elements
# Good: page.locator("[data-test='nav-cart'] .badge")  # Specific to cart
```

**Timeout Issues**
```bash
# Solution: Use element visibility waits instead of networkidle
element.wait_for(state="visible", timeout=10000)
```

**Cart Price Not Updating**
```bash
# Solution: Press Tab after quantity change to trigger update
page.keyboard.press("Tab")
time.sleep(2)  # Wait for calculation
```

## 📚 Project Highlights

### 1. Authentication Optimization
- **Before**: Login on every test (30+ seconds overhead)
- **After**: Login once, save state, reuse (instant authentication)

### 2. Organized Structure
- Clear separation: Locators → Pages → Tests
- Proper module imports with sys.path configuration
- Each layer has a single responsibility

### 3. Maintainable Code
- Page Objects encapsulate UI interactions
- Locators separated for easy updates
- Granular methods + combined helpers

### 4. Comprehensive Testing
- UI Testing: Validation, happy path, error correction
- API Testing: POST requests, validation, response verification
- Authentication: Storage state management
- Price calculation: Dynamic updates and verification

### 5. Best Practices
- Page Object Model pattern
- Fixture-based test setup
- AAA (Arrange-Act-Assert) pattern
- Specific locator strategies to avoid ambiguity

## 🤝 Contributing

This is an assessment project. For improvements:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is created for educational and assessment purposes.

## 👤 Author

**Foyez Kabir**
- Email: foyezkabir00@gmail.com
- GitHub: [@foyezkabir](https://github.com/foyezkabir)

## 🙏 Acknowledgments

- Practice Software Testing website for test environment
- Playwright and Selenium communities
- pytest framework contributors

---

**Note**: This project demonstrates test automation best practices including Page Object Model, fixture-based testing, and storage state management for authentication.
