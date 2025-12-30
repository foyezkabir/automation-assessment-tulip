# Automation Assessment Project

A comprehensive test automation framework using Playwright with Python for web application testing, featuring Page Object Model pattern and API testing.

## 🎯 Project Overview

This project demonstrates automated testing capabilities for the Practice Software Testing web application:
- **Website**: https://practicesoftwaretesting.com/
- **API**: https://api.practicesoftwaretesting.com/

## 🏗️ Project Structure

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
├── tests/                          # UI test files
│   ├── test_cart.py               # Cart functionality tests
│   └── test_contact.py            # Contact form tests
├── conftest.py                     # pytest configuration
├── test_contact_api.py             # API tests for POST messages
├── test_get_cart_api.py            # API tests for GET carts
└── requirements.txt                # Python dependencies
```

## 🚀 Features

### 1. **Page Object Model (POM) Pattern**
- Two-layer architecture: Locators (in `Locators/`) + Page Objects (in `Pages/`)
- Granular action methods for each UI element
- Combined convenience methods for complex workflows
- Proper module imports using `sys.path` configuration

### 2. **Test Coverage**

#### Contact Form Tests (`tests/test_contact.py`)
- ✅ Empty form validation
- ✅ Successful submission with valid data
- ✅ Error correction workflow

#### Cart Functionality Tests (`tests/test_cart.py`)
- ✅ Add product to cart and verify (1 item)
- ✅ Add additional quantity (2 more items = 3 total)
- ✅ Navigate between cart and product pages
- ✅ Price calculation verification ($14.15 → $42.45)
- ✅ Cart badge count updates
- ✅ Update cart quantity from cart page

#### API Tests

**POST Messages API** (`test_contact_api.py`)
- ✅ POST message with valid data
- ✅ Validation tests for missing fields
- ✅ Invalid email format handling
- ✅ Special characters support
- ✅ Response time verification
- ✅ Response headers validation

**GET Carts API** (`test_get_cart_api.py`)
- ✅ Valid cart ID retrieval
- ✅ Invalid ID format handling
- ✅ Non-existent cart handling
- ✅ Response structure validation
- ✅ Security tests (SQL injection, XSS)
- ✅ Response time and headers verification

## 📦 Installation

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)
- Git (for cloning repository)

### Setup Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/foyezkabir/automation-assessment-tulip.git
cd automation-assessment-tulip
```

#### 2. Create Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal when activated.

#### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- playwright 1.57.0
- pytest 9.0.2
- pytest-playwright 0.7.2
- requests 2.32.5
- And other required packages

#### 4. Install Playwright Browsers
```bash
playwright install chromium
```

Or install all browsers:
```bash
playwright install
```

#### 5. Verify Installation
```bash
# Check Python version
python --version

# Check pytest installation
python -m pytest --version

# Check Playwright installation
playwright --version
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

# POST Messages API tests
python -m pytest test_contact_api.py -v

# GET Carts API tests
python -m pytest test_get_cart_api.py -v
```

### Run Individual Test
```bash
# UI Tests
python -m pytest tests/test_contact.py::test_contact_form_validation_empty_fields -v
python -m pytest tests/test_cart.py::test_add_to_cart_and_verify -v

# API Tests
python -m pytest test_contact_api.py::TestMessagesAPI::test_post_message_success -v
python -m pytest test_get_cart_api.py::TestCartsGetAPI::test_get_cart_with_valid_id -v
```

### Run with Different Options
```bash
# Run with detailed output
python -m pytest tests/ -v -s

# Run only failed tests
python -m pytest --lf -v

# Run and stop on first failure
python -m pytest -x tests/

# Run with HTML report
python -m pytest tests/ --html=report.html --self-contained-html
```

## 🔧 Configuration

### Browser Settings (`conftest.py`)
Tests run in **headed mode** with slow motion for better visibility:
```python
"headless": False       # Browser window visible
"slow_mo": 500         # 500ms delay between actions
```

To run in headless mode (faster, no UI):
```python
# Edit conftest.py
"headless": True
"slow_mo": 0
```

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
- ✅ `test_add_to_cart_and_verify` - Add 1 item, verify, add 2 more (total 3), verify price updates
- ✅ `test_update_cart_quantity_and_verify_price` - Update quantity from cart: 1→3, price: $14.15→$42.45

### Contact Form Tests (`tests/test_contact.py`)
- ✅ `test_contact_form_validation_empty_fields` - All 5 required field errors shown
- ✅ `test_contact_form_successful_submission` - Success message displayed
- ✅ `test_contact_form_validation_and_correction` - Error → Fix → Success flow

### POST Messages API Tests (`test_contact_api.py`)
- ✅ 13 test cases covering validation, success, error handling
- ✅ Response time verification (< 3 seconds)
- ✅ Special characters and edge cases

### GET Carts API Tests (`test_get_cart_api.py`)
- ✅ 19 test cases covering valid/invalid scenarios
- ✅ Security testing (SQL injection, XSS attempts)
- ✅ Response structure and headers validation

## 🛠️ Technologies Used

- **Playwright** 1.57.0 - Modern browser automation framework
- **pytest** 9.0.2 - Python testing framework
- **pytest-playwright** 0.7.2 - Playwright-pytest integration
- **requests** 2.32.5 - HTTP library for API testing
- **Python** 3.12+ - Programming language

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

### 1. Organized Structure
- Clear separation: Locators → Pages → Tests
- Proper module imports with sys.path configuration
- Each layer has a single responsibility
- Tests organized in separate `tests/` folder

### 2. Maintainable Code
- Page Objects encapsulate UI interactions
- Locators separated for easy updates
- Granular methods + combined convenience helpers
- Reusable fixtures for test setup

### 3. Comprehensive Testing
- **UI Testing**: Validation, happy path, error correction workflows
- **API Testing**: POST/GET requests, validation, response verification
- **E-commerce flows**: Cart operations, price calculations, quantity updates
- **Security testing**: SQL injection and XSS attempts in API tests

### 4. Best Practices
- Page Object Model (POM) pattern
- Fixture-based test setup with pytest
- AAA (Arrange-Act-Assert) pattern
- Specific locator strategies to avoid ambiguity
- Time delays where needed for UI stability

### 5. Real-World Scenarios
- Add to cart workflow with multiple steps
- Cart quantity updates and price recalculation
- Form validation with error handling
- API endpoint testing with edge cases

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
