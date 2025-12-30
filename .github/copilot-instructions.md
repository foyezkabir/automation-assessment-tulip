# Copilot Instructions for Automation Assessment Project

## Project Overview
Playwright + Selenium test automation framework for web applications with authentication state management and Page Object Model pattern.

## Architecture & Structure

```
├── tests/              # Test files (preferred location)
├── Pages/              # Page Object Models with methods
├── Locators/           # Locator classes (legacy, being phased out)
├── auth_helper.py      # Authentication utilities
├── auth_state.json     # Cached JWT tokens & localStorage
└── conftest.py         # pytest global configuration
```

**Key Pattern**: Tests import directly from root-level files (e.g., `from contactPage import ContactPage`), NOT from subdirectories. Page Objects in `Pages/` define methods, while locator definitions are in `Locators/`.

## Critical Workflows

### Running Tests
```bash
# Use module invocation (pytest command may not be in PATH)
python -m pytest test_file.py -v
python -m pytest test_file.py::test_function_name -v
```

### Browser Configuration (conftest.py)
- **Headed mode**: `headless: False` with `slow_mo: 500` for visibility
- Tests run slowly intentionally for demo/debugging purposes

### Authentication Pattern
1. **First run**: `test_login_and_save_state()` logs in and saves to `auth_state.json`
2. **Subsequent tests**: Use `authenticated_context` fixture to load saved state
3. **Storage state contains**: JWT tokens (id_token, access_token, refresh_token), localStorage, Redux state

```python
# Example: Using saved auth
@pytest.fixture
def authenticated_context(browser):
    context = get_authenticated_context(browser, "auth_state.json")
    yield context
```

## Page Object Model Pattern

### Two-Layer Approach
1. **Locators class** (`Locators/*.py`): Defines element selectors using `data-test` attributes
2. **Page class** (`Pages/*.py`): Imports locators, defines granular action methods

### Page Object Structure
```python
# Import locators at top
import contactLoc from contactLoc

class ContactPage:
    def __init__(self, page: Page):
        self.page = page
    
    # Granular methods for each action
    def fill_first_name(self, value: str):
        self.first_name.fill(value)
    
    # Combined convenience methods
    def fill_complete_form(self, first_name, last_name, email, subject, message):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        # ... etc
```

**Important**: Access locators directly via properties, NOT through nested objects (e.g., `self.first_name`, not `self.locators.first_name`)

## Test Writing Conventions

### Fixture-Based Setup
Tests use pytest fixtures for page setup instead of decorators:
```python
@pytest.fixture
def contact(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()
    contact_page.click_nav_contact()
    return contact_page

def test_something(contact: ContactPage):
    # Test receives ready ContactPage instance
    contact.fill_first_name("John")
```

### Test Structure (AAA Pattern)
```python
def test_name(fixture):
    # Arrange - setup test data
    test_data = {"first_name": "John", ...}
    
    # Act - perform actions
    contact.fill_complete_form(**test_data)
    contact.click_submit()
    
    # Assert - verify results
    contact.expect_success_message()
```

### Scrolling for Visibility
When validation errors appear after form submission:
```python
contact.click_submit()
time.sleep(1)  # Wait for errors to render
contact.page.evaluate("window.scrollTo(0, 0)")  # Scroll to top
time.sleep(1)
```

## Locator Strategy
- **Primary**: `data-test` attributes (e.g., `[data-test='first-name']`)
- **Auth forms**: `get_by_role()` for accessibility (e.g., `get_by_role("textbox", name="Email")`)
- **Validation messages**: `get_by_text()` for exact text matching

## Common Pitfalls
1. **Import errors**: Page Objects and tests should import from root, not from `Pages/` or `Locators/` subdirectories
2. **Fixture confusion**: Don't use decorators that conflict with pytest's fixture system - use fixtures instead
3. **Select options**: After validation errors, dropdown may need page refresh or explicit re-selection
4. **Headless mode**: Tests run in headed mode by default for visibility - change in `conftest.py` if needed

## Test Applications
- **Practice site**: `https://practicesoftwaretesting.com/` (contact form tests)
- **Auth app**: `https://bprp-prod.shadhinlab.xyz/` (login with AWS Cognito)

## Dependencies
- Playwright 1.57.0 with pytest-playwright
- Selenium 4.39.0 with webdriver-manager
- pytest 9.0.2 for test framework
