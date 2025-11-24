# 🧵 Polyester Automation Framework  
### End-to-End UI + API Test Automation | Playwright + Pytest + Allure + GitHub Actions

[![CI Pipeline](https://github.com/AnastasiiaDemenkova/polyester-automation/actions/workflows/run-tests.yml/badge.svg)](https://github.com/AnastasiiaDemenkova/polyester-automation/actions/workflows/run-tests.yml)
[![Nightly Regression](https://github.com/AnastasiiaDemenkova/polyester-automation/actions/workflows/nightly.yml/badge.svg)](https://github.com/AnastasiiaDemenkova/polyester-automation/actions/workflows/nightly.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-blue)](https://anastasiiademenkova.github.io/polyester-automation/allure-report/)

A complete Python-based UI + API automation framework built from scratch for testing  
**https://polyester.com** — created to simulate a real professional automation project using modern CI/CD.

---

## 🚀 Tech Stack
- **Python 3.10**
- **Pytest** — test runner  
- **Playwright** — UI test automation  
- **Requests** — API test automation  
- **Allure** — reporting  
- **GitHub Actions** — full CI/CD pipelines  
- Environment-based test execution (**dev / preprod / prod**)  

---

# 📁 Project Structure

polyester-automation/
│
├── tests/
│ ├── ui/ # UI tests (Playwright)
│ └── api/ # API tests (Requests)
│
├── configs/ # Environment configs
│ ├── dev.env
│ ├── preprod.env
│ └── prod.env
│
├── utils/
│ └── env_loader.py # Loads environment + URLs
│
├── .github/
│ └── workflows/ # CI/CD pipelines
│ ├── run-tests.yml # PR + Push tests
│ ├── nightly.yml # Nightly regression
│ └── deploy-allure-report.yml
│
├── pytest.ini # Pytest settings + markers
├── requirements.txt # Dependencies
└── README.md

yaml
Copy code

---

# 🧪 Running Tests Locally

### **1. Install dependencies**
```bash
pip install -r requirements.txt
playwright install
2. Run all tests
bash
Copy code
pytest
3. Run smoke tests
bash
Copy code
pytest -m smoke
4. Generate Allure report
bash
Copy code
pytest --alluredir=allure-results
allure serve allure-results
🔁 CI/CD Workflows (GitHub Actions)
✔ On Pull Requests
Runs smoke tests only

Fast validation before merge

✔ On Push to main
Runs UI + API full suite

Generates Allure artifacts

✔ Nightly Regression (Scheduled)
Runs a full regression suite every night

Uploads Allure results as an artifact

Automatically publishes Allure Report to GitHub Pages

✔ Allure Report Deployment
Nightly report is published here:

👉 https://anastasiiademenkova.github.io/polyester-automation/allure-report/

📊 Example Architecture (CI + Tests)
mermaid
Copy code
flowchart TD

A[Developer Commit / Pull Request] --> B[GitHub Actions CI]

B -->|PR| C[Smoke Tests]
B -->|Push to main| D[UI + API Tests]
B -->|Nightly| E[Full Regression]

E --> F[Upload Allure Results]
F --> G[Deploy Allure Report to GitHub Pages]

G --> H[Public Nightly Allure Report]
🪄 Test Strategy Summary
✔ UI Testing (Playwright)
Homepage validation

Navigation

Elements visibility

Mobile/desktop viewport testing

Smoke suite for PRs

Regression for nightly

✔ API Testing (Requests)
Status codes

Headers

Response validation

Error handling

Contract testing (future)

✔ Non-Functional (Future)
Performance testing

Load testing (k6 / Locust)

Visual regression

🗺 Roadmap (Planned Enhancements)
Add Code Coverage (Codecov)

Add Docker setup

Add multi-browser matrix (Chrome, Firefox, WebKit)

Add screenshot-based visual testing

Add data-driven testing

Add retry logic for flaky UI tests

👩‍💻 Author
Anastasiia Demenkova
Senior QA Automation Engineer
Santa Clara, CA
