# Polyester Automation Framework

[![CI Status](https://github.com/AnastasiiaDemenkova/polyester-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/AnastasiiaDemenkova/polyester-automation/actions/workflows/tests.yml)
[![Nightly Regression](https://github.com/AnastasiiaDemenkova/polyester-automation/actions/workflows/nightly.yml/badge.svg)](https://github.com/AnastasiiaDemenkova/polyester-automation/actions/workflows/nightly.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-blue)](https://anastasiiademenkova.github.io/polyester-automation/allure-report/)
![Coverage](https://img.shields.io/badge/Coverage-Coming%20Soon-red)

A complete **UI + API automation framework** built from scratch for testing **Polyester.com**, designed to simulate a real-world QA Automation project with **industry-standard CI/CD practices**.

---

## 🚀 Tech Stack

- **Python + Pytest**
- **Playwright** (UI automation)
- **Requests** (API automation)
- **Allure Reporting**
- **GitHub Actions (CI/CD)**
- **Environment-based Testing (dev / preprod / prod)**

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
│ └── env_loader.py # Loads ENV variables dynamically
│
├── .github/
│ └── workflows/ # CI/CD pipelines
│
├── pytest.ini # Pytest config & markers
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🧪 Running Tests Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
playwright install
2. Run all tests
bash
Copy code
pytest
3. Run smoke tests only
bash
Copy code
pytest -m smoke
4. Generate Allure report
bash
Copy code
pytest --alluredir=allure-results
allure serve allure-results
🔁 CI/CD Pipelines (GitHub Actions)
✔ Pull Requests
Runs smoke tests only (fastest feedback).

✔ Push to main
Runs full UI + API suite, uploads Allure results + artifacts.

✔ Nightly Regression (scheduled)
Runs full regression, uploads results.

✔ Allure Report Deployment
Deploys latest nightly report to GitHub Pages.

📊 Allure Report (Nightly)
👉 Live Report
https://anastasiiademenkova.github.io/polyester-automation/allure-report/

🗺 Future Enhancements
Add code coverage (Codecov)

Add Docker support

Add multi-browser (Chrome, Firefox, Safari)

Add Visual Regression Testing

Add Load Testing (Locust/k6)

👩‍💻 Author
Anastasiia Demenkova
QA Automation Engineer
Santa Clara, CA
