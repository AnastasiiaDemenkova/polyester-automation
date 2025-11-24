Polyester Automation Framework






A complete UI + API automation framework built from scratch for testing Polyester.com, designed to simulate a real-world QA Automation project with industry-standard CI/CD practices.

🚀 Tech Stack

Python + Pytest

Playwright (UI automation)

Requests (API automation)

Allure Reporting

GitHub Actions (CI/CD)

Environment-based testing (dev / preprod / prod)

📁 Project Structure
polyester-automation/
│
├── tests/
│   ├── ui/        # UI tests (Playwright)
│   └── api/       # API tests (Requests)
│
├── configs/       # Environment configs (dev / preprod / prod)
│
├── utils/
│   └── env_loader.py  # Loads environment variables
│
├── .github/
│   └── workflows/     # CI/CD pipelines
│
├── pytest.ini         # Test config & markers
├── requirements.txt
└── README.md

🧪 Running Tests Locally
1. Install dependencies
pip install -r requirements.txt
playwright install

2. Run all tests (UI + API)
pytest

3. Run smoke tests only
pytest -m smoke

4. Generate Allure Report
pytest --alluredir=allure-results
allure serve allure-results

🔁 CI/CD Pipeline Overview (GitHub Actions)
✔ On Pull Requests

Runs smoke tests only for fast feedback.

✔ On Push to main

Runs full UI + API suite, generates Allure results.

✔ Nightly Regression (Scheduled)

Runs full regression, uploads Allure artifacts.

✔ Allure Report Deployment

Publishes nightly Allure report to GitHub Pages.

📊 Allure Report (Nightly)

👉 Latest Nightly Test Report:
https://anastasiiademenkova.github.io/polyester-automation/allure-report/

🗺 Future Enhancements

Add Code Coverage (Codecov)

Add Docker support

Add multi-browser testing (Chrome / Firefox / Safari)

Add visual regression (Playwright screenshots)

Add load testing (Locust or k6)

💡 Author

Anastasiia Demenkova
QA Automation Engineer
Santa Clara, CA
