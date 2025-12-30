# Automation Assessment Project

A comprehensive test automation framework using Playwright and Selenium with Python for web application testing, featuring authentication state management and Page Object Model pattern.

## 🎯 Project Overview

This project demonstrates automated testing capabilities for two web applications:
1. **Practice Software Testing** (https://practicesoftwaretesting.com/) - E-commerce testing
2. **BPRP Production** (https://bprp-prod.shadhinlab.xyz/) - Authentication with AWS Cognito

## 🏗️ Architecture

```
automation-assessment/
├── .github/
│   └── copilot-instructions.md    # AI agent guidelines
├── Pages/                          # Page Object Models
│   ├── contactPage.py             # Contact form page actions
│   └── cartPage.py                # Product & cart page actions
├── Locators/                       # Element locators (legacy)
│   ├── contactLoc.py
│   └── cartLoc.py
├── tests/                          # Test files
│   └── test_contact.py            # Contact form tests
├── auth_helper.py                  # Authentication utilities
├── auth_state.json                 # Cached JWT tokens
├── conftest.py                     # pytest configuration
├── test_login_playwright.py        # Login & storage state tests
├── test_cart.py                    # Cart functionality tests
├── test_playwright.py              # Basic Playwright tests
├── test_selenium.py                # Basic Selenium tests
└── requirements.txt                # Python dependencies
```

## 🚀 Features

### 1. **Page Object Model (POM) Pattern**
- Two-layer architecture: Locators + Page Objects
- Granular action methods for each UI element
- Combined convenience methods for complex workflows
- Direct property access for locators

### 2. **Authentication State Management**
- Single login with JWT token caching
- Reusable authentication across tests
- Storage state persists: id_token, access_token, refresh_token
- No repeated login overhead

### 3. **Test Categories**

#### Contact Form Tests (`test_contact.py`)
- ✅ Empty form validation
- ✅ Successful submission with valid data
- ✅ Error correction workflow

#### Cart Functionality Tests (`test_cart.py`)
- ✅ Add product to cart and verify
- ✅ Update cart quantity (1 → 3)
- ✅ Add multiple quantities directly
- ✅ Price calculation verification

#### Authentication Tests (`test_login_playwright.py`)
- ✅ Login and save storage state
- ✅ Reuse authentication context
- ✅ Navigate protected routes without login

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
python -m pytest test_contact.py -v

# Cart functionality tests
python -m pytest test_cart.py -v

# Authentication tests
python -m pytest test_login_playwright.py -v
```

### Run Individual Test
```bash
python -m pytest test_contact.py::test_contact_form_validation_empty_fields -v
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

2. **Auth forms**: `get_by_role()` for accessibility
   ```python
   page.get_by_role("textbox", name="Email")
   ```

3. **Validation messages**: `get_by_text()` for exact matching
   ```python
   page.get_by_text("First name is required")
   ```

### Import Pattern
```python
# Import from root level (not subdirectories)
from contactPage import ContactPage
from cartPage import CartPage
```

## 📊 Test Results

### Cart Tests
- ✅ `test_add_to_cart_and_verify` - Verifies product appears in cart
- ✅ `test_update_cart_quantity_and_verify_price` - Updates quantity: 1→3, price: $14.15→$42.45
- ✅ `test_add_multiple_quantity_to_cart` - Adds 2 items, verifies total: $28.30

### Contact Form Tests
- ✅ `test_contact_form_validation_empty_fields` - All 5 required field errors shown
- ✅ `test_contact_form_successful_submission` - Success message displayed
- ✅ `test_contact_form_validation_and_correction` - Error → Fix → Success flow

## 🛠️ Technologies Used

- **Playwright** 1.57.0 - Modern browser automation
- **Selenium** 4.39.0 - Cross-browser testing
- **pytest** 9.0.2 - Test framework
- **pytest-playwright** 0.7.2 - Playwright-pytest integration
- **webdriver-manager** 4.0.2 - Automatic driver management

## 🐛 Debugging

### View Test Execution
Tests run in **headed mode** with 500ms slow motion by default for visibility.

### Common Issues

**Import Errors**
```bash
# Solution: Tests must be at root level to import Page Objects
# Move test files from tests/ to root if needed
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

### 2. Maintainable Structure
- Page Objects encapsulate UI interactions
- Locators separated for easy updates
- Granular methods + combined helpers

### 3. Comprehensive Testing
- Validation testing (negative scenarios)
- Happy path testing (positive scenarios)
- Error correction workflows
- Price calculation verification

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
