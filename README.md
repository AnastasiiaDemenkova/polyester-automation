# Polyester Automation Framework
End-to-End UI and API Test Automation using Playwright, Pytest, Requests, Allure, and GitHub Actions.

This project demonstrates a clean, production-ready Python automation framework with CI/CD integration across environments.

## Tech Stack
- Python 3.10+
- Pytest (test runner)
- Playwright (UI automation)
- Requests (API testing)
- Allure (reporting)
- GitHub Actions (CI/CD)
- Environment-based test execution (dev, preprod, prod)

## Project Structure
polyester-automation/
│
├── tests/
│ ├── ui/ # Playwright UI test suite
│ └── api/ # API tests using requests
│
├── configs/ # Environment configurations
│ ├── dev.env
│ ├── preprod.env
│ └── prod.env
│
├── utils/
│ └── env_loader.py # Loads environment variables and URLs
│
├── .github/
│ └── workflows/ # GitHub Actions pipeline files
│
├── requirements.txt
└── README.md

markdown
Copy code

## Test Coverage

### UI Tests (Playwright)
- Login flow validation
- Navigation checks
- Regression validation
- Error and edge-case flows
- Browser compatibility

### API Tests (Requests)
- Positive response validation
- Invalid API key returns 401
- Missing Referer header returns 401
- No headers returns 401
- Basic performance threshold (< 5 seconds)

## Installation
Install all dependencies:
pip install -r requirements.txt

yaml
Copy code

Install Playwright browsers:
playwright install

python
Copy code

## Running Tests

Run all tests:
pytest

sql
Copy code

Run only UI tests:
pytest -m ui

sql
Copy code

Run only API tests:
pytest -m api

yaml
Copy code

Generate Allure report:
pytest --alluredir=allure-results
allure serve allure-results

powershell
Copy code

## Environment Switching
Set the environment before running tests:
ENV=dev pytest

yaml
Copy code

Environment loader:
utils/env_loader.py

markdown
Copy code

## CI/CD Pipeline
GitHub Actions pipeline includes:
- Installing dependencies
- Running UI and API tests
- Saving Allure reports as artifacts
- Nightly regression execution

Workflow file location:
.github/workflows/tests.yml

markdown
Copy code

## Reports
- Allure test reports
- Screenshots on UI test failure
- API logs and response validation
- Optional Playwright trace artifacts

## Future Enhancements
- Add Docker support
- Add Playwright trace viewer uploads
- Parallel test execution in CI
- Expand API coverage
- Add LLM response validation for chatbot testing

## Author
Created by Anastasiia Demenkova  
Senior QA Engineer specializing in Web, Mobile, API, and AI/LLM Quality Assurance.

LinkedIn: https://www.linkedin.com/in/anastasiia-demenkova-036a9b120  
Portfolio: https://anastasiiademenkova.com
