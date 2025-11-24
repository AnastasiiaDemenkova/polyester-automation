# Polyester Automation Framework

![CI](https://github.com/AnastasiiaDemenkova/polyester-automation/actions/workflows/tests.yml/badge.svg)
[![Allure Report](https://img.shields.io/badge/Allure-Report-ff69b4.svg)](https://anastasiiademenkova.github.io/polyester-automation/allure-report/)
![Coverage](https://img.shields.io/badge/Coverage-Coming%20Soon-blue)

A complete UI + API automation framework built from scratch for testing **Polyester.com**, designed to simulate a real-world QA Automation project with industry-standard CI/CD practices.

---

## 🚀 Tech Stack

- **Python + Pytest**
- **Playwright** (UI automation)
- **Requests** (API automation)
- **Allure Reporting**
- **GitHub Actions (CI/CD)**
- **Environment-based testing (dev / preprod / prod)**

---

## 📁 Project Structure

polyester-automation/
│
├── tests/
│ ├── ui/ # UI tests (Playwright)
│ └── api/ # API tests (Requests)
│
├── configs/ # Environment configs (dev / preprod / prod)
│
├── utils/
│ └── env_loader.py # Loads environment variables
│
├── .github/workflows/ # CI/CD pipelines
│
├── pytest.ini # Test config & markers
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🧪 Running Tests Locally

### Install dependencies
```bash
pip install -r requirements.txt
playwright install
Run UI + API tests
bash
Copy code
pytest
Run smoke tests only
bash
Copy code
pytest -m smoke
Generate Allure report
bash
Copy code
pytest --alluredir=allure-results
allure serve allure-results
🔁 CI/CD Pipelines (GitHub Actions)
✔ On Pull Requests
Runs smoke tests only for fast validation.

✔ On Push to main
Runs full UI + API suite, generates Allure results.

✔ Nightly Regression (Scheduled)
Runs full regression, uploads Allure artifacts.

✔ Allure Report Deployment
Publishes nightly Allure report to GitHub Pages.

📊 Allure Report (Nightly)
Click to view the latest nightly test report:

👉 https://anastasiiademenkova.github.io/polyester-automation/allure-report/

🗺 Future Enhancements
Add Code Coverage (Codecov)

Add Docker support

Add multi-browser matrix (Chrome, Firefox, Safari)

Add Visual Regression Testing (Playwright screenshots)

Add Load Testing with Locust or k6

💡 Author
Anastasiia Demenkova
QA Automation Engineer
Santa Clara, CA
