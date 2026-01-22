# Automation Assessment - Playwright JavaScript

High-performance test automation framework built with **Playwright** and **JavaScript**, featuring Page Object Model architecture, parallel test execution, and enhanced reporting with Smart Reporter.

## 🎯 Overview

This framework provides:
- **Fast execution** - Optimized test runs with parallel execution
- **Page Object Model** - Maintainable and reusable test code
- **Smart Reporting** - Enhanced test reports with visual analytics
- **Modern async/await** - Clean JavaScript patterns
- **Multiple browsers** - Chromium, Firefox, WebKit support

## 📁 Project Structure

```
├── tests/                          # Test suites
│   ├── test-contact.spec.js       # Contact form validation tests
│   ├── test-cart.spec.js          # Shopping cart functionality tests
│   ├── smart-report.html          # Test report dashboard
│   └── test-history.json          # Test execution history
├── Pages/                          # Page Object Models
│   ├── contactPage.js             # Contact page actions & assertions
│   └── cartPage.js                # Cart page actions & assertions
├── Locators/                       # Locator definitions (for complex pages)
│   └── cartLoc.js                 # Cart page element selectors
├── playwright.config.js            # Playwright configuration
├── package.json                    # Node.js dependencies & scripts
├── node_modules/                   # Dependencies (auto-generated)
├── playwright-report/              # HTML test reports
├── test-results/                   # Screenshots, videos, traces
└── README.md                       # This file
```

## 🔧 Installation

### Prerequisites
- **Node.js** (v16 or higher recommended)
- **npm** (comes with Node.js)

### Setup Steps
```bash
# 1. Install all dependencies
npm install

# 2. Install Playwright browsers (Chromium, Firefox, WebKit)
npx playwright install

# 3. Install Smart Reporter (if not already installed)
npm install playwright-smart-reporter

# 4. Run tests to verify setup
npm test
npm run test:headed

# Run specific test file
npm run test:contact
npm run test:cart

# Debug mode
npm run test:debug

# View HTML report
npm run report
```

### Command Line Options
```bash
# Run specific test
npx playwright test tests/test-contact.spec.js

# Run with UI mode
npx playwright test --ui

# Run in headed mode
npx playwright test --headed

# Run with specific browser
npx playwright test --project=chromium
```

## ⚡ Parallel Test Execution

### What is Parallel Execution?
Parallel execution allows multiple test files to run simultaneously using separate worker processes, significantly reducing total test execution time.

### Benefits
- **Faster test runs** - Multiple tests execute at the same time
- **Better resource utilization** - Uses multiple CPU cores
- **Scalable** - Add more workers as test suite grows
- **Time savings** - 4 tests in ~27 seconds instead of running sequentially

### How to Configure
```javascript
// playwright.config.js
module.exports = defineConfig({
  fullyParallel: true,       // Enable parallel execution
  workers: 2,                 // Number of parallel workers (adjust based on CPU)
  // workers: process.env.CI ? 1 : 2,  // Use 1 worker in CI, 2 locally
});
```

### Worker Configuration Guidelines
- **2 workers**: Good for local development (4-8 CPU cores)
- **4 workers**: For machines with 8+ CPU cores
- **1 worker**: For CI/CD or sequential execution
- **Auto**: `workers: undefined` - Playwright decides based on CPU count

### Running Tests in Different Modes

```bash
# Fast mode (headless, parallel) - DEFAULT
npm test

# Visual mode (headed, see browser)
npx playwright test --headed

# Debug mode (headed, slow, interactive)
npm run test:debug

# UI mode (interactive test runner)
npx playwright test --ui
```

## 📊 Smart Reporter Integration

### Features
The project integrates `playwright-smart-reporter` for enhanced test reporting:

- **📈 Visual Test Analytics**: Detailed execution metrics and trends
- **🖼️ Screenshot Capture**: Automatic screenshots on test failure
- **🎥 Video Recording**: Records video for failed tests
- **📝 Execution History**: Tracks test results over time via `test-history.json`
- **🔍 Detailed Logs**: Step-by-step action logs for debugging

### Viewing Reports

```bash
# View Smart Report (generated after each test run)
Start-Process ".\tests\smart-report.html"

# Or open in default browser
.\tests\smart-report.html

# View standard Playwright HTML report
npx playwright show-report
```

### Report Location
- **Smart Report**: `tests/smart-report.html`
- **Standard HTML Report**: `playwright-report/index.html`
- **Test History**: `tests/test-history.json`

## 🧪 Running Tests

### Basic Commands
```bash
# Run all tests (fast mode: headless + parallel)
npm test

# Run tests with browser visible
npx playwright test --headed

# Run specific test file
npx playwright test tests/test-contact.spec.js
npx playwright test tests/test-cart.spec.js

# Run tests in debug mode (slow + interactive)
npx playwright test --debug

# Run with UI mode (interactive)
npx playwright test --ui

# View reports
npm run report  # Opens last HTML report
```

### NPM Scripts
```json
{
  "scripts": {
    "test": "npx playwright test",
    "test:headed": "npx playwright test --headed",
    "test:contact": "npx playwright test tests/test-contact",
    "test:cart": "npx playwright test tests/test-cart",
    "test:debug": "npx playwright test --debug",
    "report": "npx playwright show-report"
  }
}
```

## 🏗️ Page Object Model Architecture

### Two-Layer Design Pattern

#### 1. Locators Layer (Optional - for complex pages)
```javascript
// Locators/cartLoc.js
class CartLocators {
  constructor(page) {
    this.page = page;
    this.addToCartBtn = page.locator("[data-test='add-to-cart']");
    this.cartBadge = page.locator("[data-test='nav-cart'] .badge");
  }
}
```

#### 2. Page Object Layer (Required - actions + assertions)
```javascript
// Pages/contactPage.js
const { expect } = require('@playwright/test');

class ContactPage {
  constructor(page) {
    this.page = page;
    this.firstName = page.locator("[data-test='first-name']");
  }
  
  // Granular action methods
  async fillFirstName(value) {
    await this.firstName.fill(value);
  }
  
  // Assertion methods
  async expectFirstNameError() {
    await expect(this.page.getByText('First name is required')).toBeVisible();
  }
  
  // Combined convenience methods
  async fillCompleteForm({ firstName, lastName, email, subject, message }) {
    await this.fillFirstName(firstName);
    await this.fillLastName(lastName);
    await this.fillEmail(email);
    await this.selectSubject(subject);
    await this.fillMessage(message);
  }
}

module.exports = { ContactPage };
```

## ✍️ Test Writing Patterns

### Test Structure (AAA Pattern)
```javascript
const { test, expect } = require('@playwright/test');
const { ContactPage } = require('../Pages/contactPage');

## ✍️ Test Writing Patterns

### Test Structure (AAA Pattern)
```javascript
const { test, expect } = require('@playwright/test');
const { ContactPage } = require('../Pages/contactPage');

test.describe('Contact Form Tests', () => {
  let contactPage;

  test.beforeEach(async ({ page }) => {
    // Setup: Initialize page object and navigate
    contactPage = new ContactPage(page);
    await contactPage.goto();
    await contactPage.clickNavContact();
  });

  test('Verify validation errors on empty form submission', async () => {
    // Arrange - No data needed for empty form test
    
    // Act - Submit empty form
    await contactPage.clickSubmit();
    await contactPage.page.evaluate(() => window.scrollTo(0, 0));
    
    // Assert - Verify all error messages appear
    await contactPage.verifyAllRequiredErrors();
  });

  test('Verify successful form submission with valid data', async () => {
    // Arrange - Prepare test data
    const testData = {
      firstName: 'John',
      lastName: 'Doe',
      email: 'john.doe@example.com',
      subject: 'webmaster',
      message: 'Test message content'
    };
    
    // Act - Fill and submit form
    await contactPage.fillCompleteForm(testData);
    await contactPage.clickSubmit();
    
    // Assert - Verify success message
    await contactPage.expectSuccessMessage();
  });
});
```

## 🎯 Locator Strategy

Tests use a hierarchy of locator strategies for maximum stability:

1. **Primary: `data-test` attributes** (Most stable)
   ```javascript
   page.locator("[data-test='first-name']")
   page.locator("[data-test='add-to-cart']")
   ```

2. **Accessibility roles** (Semantic HTML)
   ```javascript
   page.getByRole('button', { name: 'Submit' })
   page.getByRole('textbox', { name: 'Email' })
   ```

3. **Text content** (For validation messages)
   ```javascript
   page.getByText('First name is required')
   page.getByText('Thanks for your message!')
   ```

4. **CSS selectors** (Last resort)
   ```javascript
   page.locator('.card-title')
   page.locator('h1')
   ```

## 🌐 Test Applications

### Practice Software Testing Site
**URL**: `https://practicesoftwaretesting.com/`

#### Contact Form Tests
- Empty form validation
- Successful submission with valid data
- Error correction workflow
- Field-level validation

#### Shopping Cart Tests
- Add single item to cart
- Add multiple quantities
- Cart badge counter verification
- Price calculation verification

## ⚙️ Configuration

### Playwright Config Highlights
```javascript
// playwright.config.js
module.exports = defineConfig({
  testDir: './tests',
  fullyParallel: true,           // Run tests in parallel
  workers: 2,                     // Use 2 worker processes
  
  reporter: [
    ['html'],                     // Standard HTML report
    ['list'],                     // Console output
    ['playwright-smart-reporter'] // Enhanced smart reporter
  ],
  
  use: {
    baseURL: 'https://practicesoftwaretesting.com/',
    trace: 'on-first-retry',      // Trace for debugging
    screenshot: 'only-on-failure', // Save screenshots on fail
    video: 'retain-on-failure',   // Save videos on fail
    actionTimeout: 10000,         // 10s timeout per action
  },
  
  projects: [
    {
      name: 'chromium',
      use: {
        headless: true,           // Fast headless execution
      }
    }
  ]
});
```

## 🔧 Troubleshooting

### Common Issues & Solutions

#### 1. Module Not Found Errors
```bash
# Solution: Install dependencies
npm install
```

#### 2. Browser Not Installed
```bash
# Solution: Install Playwright browsers
npx playwright install
```

#### 3. Tests Timing Out
**Possible causes:**
- Slow network connection
- Incorrect selectors
- Page not loading

**Solutions:**
```javascript
// Increase timeout in playwright.config.js
use: {
  actionTimeout: 20000,  // Increase from 10s to 20s
}

// Or per-test timeout
test('My test', async ({ page }) => {
  test.setTimeout(60000);  // 60 seconds
  // ...
});
```

#### 4. Tests Fail in Headless But Pass in Headed Mode
**Common cause:** Timing issues or viewport differences

**Solutions:**
```javascript
// Set viewport size explicitly
use: {
  viewport: { width: 1920, height: 1080 }
}

// Use proper waits instead of timeouts
await page.waitForLoadState('networkidle');
```

#### 5. Import/Export Errors
This project uses **CommonJS** syntax (not ES6 modules):
```javascript
// ✅ Correct
const { ContactPage } = require('../Pages/contactPage');
module.exports = { ContactPage };

// ❌ Wrong
import { ContactPage } from '../Pages/contactPage';
export { ContactPage };
```

## 📚 Key Dependencies

```json
{
  "devDependencies": {
    "@playwright/test": "^1.57.0"
  },
  "dependencies": {
    "playwright-smart-reporter": "^1.0.0"
  }
}
```

### What Each Package Does

- **@playwright/test**: Core Playwright testing framework
  - Browser automation (Chromium, Firefox, WebKit)
  - Test runner with parallel execution
  - Built-in assertions and auto-waiting
  - Screenshot, video, and trace recording

- **playwright-smart-reporter**: Enhanced test reporting
  - Visual analytics dashboard
  - Test history tracking
  - Detailed execution logs
  - Smart insights and recommendations

##  Best Practices

### 1. Page Object Methods Should Be Atomic
```javascript
// ✅ Good: Single responsibility
async fillFirstName(value) {
  await this.firstName.fill(value);
}

// ❌ Bad: Multiple actions
async fillFormAndSubmit(data) {
  await this.fillFirstName(data.firstName);
  await this.fillLastName(data.lastName);
  await this.submit();
}
```

### 2. Use Descriptive Test Names
```javascript
// ✅ Good: Clear intention
test('Verify validation errors appear on empty form submission', ...)

// ❌ Bad: Vague
test('Test form', ...)
```

### 3. Avoid Hardcoded Waits
```javascript
// ✅ Good: Smart waits
await expect(element).toBeVisible();
await page.waitForURL('**/checkout');

// ❌ Bad: Arbitrary timeouts
await page.waitForTimeout(3000);
```

### 4. Use data-test Attributes
```javascript
// ✅ Good: Stable selector
page.locator("[data-test='submit-button']")

// ⚠️ Fragile: Can break with design changes
page.locator('.btn.btn-primary.mt-3')
```

## 🤝 Contributing

When adding new tests or features:

1. **Follow the POM pattern**: Create page objects for new pages
2. **Write descriptive tests**: Use AAA pattern (Arrange, Act, Assert)
3. **Add proper waits**: Leverage Playwright's auto-waiting
4. **Use stable locators**: Prefer `data-test` attributes
5. **Test in both modes**: Verify tests pass in headless and headed
6. **Update documentation**: Keep README.md current

## 📄 License

ISC
