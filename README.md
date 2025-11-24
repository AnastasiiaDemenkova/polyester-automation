# Polyester Automation Framework

[![CI](https://img.shields.io/badge/CI-GitHub_Actions-blue)](https://github.com/AnastasiiaDemenkova/polyester-automation/actions)
[![Allure Report](https://img.shields.io/badge/Allure-Report-blue)]()
[![Coverage](https://img.shields.io/badge/Coverage-Coming_Soon-lightgray)]()


End-to-end UI and API automation for Polyester.com using Playwright, Pytest, Requests, Allure, and GitHub Actions. The suite is environment-aware (dev / preprod / prod) and ready for local runs or CI/CD.

---

## Tech Stack

- Python 3.10+ with Pytest
- Playwright via `pytest-playwright` for UI flows
- Requests for API checks
- Allure for reporting
- GitHub Actions for CI/CD
- Config-driven environments: `dev`, `preprod`, `prod`

---

## Repository Layout

```
polyester-automation/
├── configs/              # Environment configs (.env style)
├── tests/
│   ├── api/              # API checks (Requests)
│   └── ui/               # UI tests (Playwright)
├── utils/
│   └── env_loader.py     # Loads BASE_URL from configs/<env>.env
├── pytest.ini            # Pytest defaults + markers + Allure dir
├── playwright.config.py  # Playwright artifacts on failure
├── requirements.txt
└── README.md
```

---

## Getting Started

1) Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2) Install dependencies and Playwright browsers:

```bash
pip install -r requirements.txt
playwright install
```

---

## Running Tests

- Full suite: `pytest`
- Smoke subset: `pytest -m smoke`
- UI only: `pytest tests/ui`
- API only: `pytest tests/api`

### Choose an Environment

Configs live in `configs/<env>.env` (`dev`, `preprod`, `prod`). Tests currently call `load_environment("preprod")`; update that helper call in tests (or parameterize it) to target another environment.

Example config (`configs/dev.env`):

```
ENV=dev
BASE_URL=https://polyester.com
```

### Allure Reporting

```bash
pytest --alluredir=allure-results
allure serve allure-results   # requires Allure CLI
```

---

## CI/CD

- Pull requests: smoke tests for quick validation.
- Push to `main`: full UI + API suite with Allure artifacts.
- Nightly regression: full run; publishes Allure report to GitHub Pages.
- Latest nightly report: https://anastasiiademenkova.github.io/polyester-automation/allure-report/

---

## Coverage Highlights (current tests)

- UI: Homepage title verification (Playwright)
- API: Base URL status code check (Requests)

---

## Pytest Markers

- `ui` — UI flows in Playwright
- `api` — API checks with Requests
- `smoke` — critical path coverage
- `regression` — broader suite

---

## Future Enhancements

- Dockerized local runs
- Parallel and matrix execution (multi-browser)
- Expanded API coverage and visual regression
- Playwright trace uploads in CI

---

## Author

Anastasiia Demenkova — QA Automation Engineer (Santa Clara, CA)  
LinkedIn: https://www.linkedin.com/in/anastasiia-demenkova-036a9b120  
Portfolio: https://anastasiiademenkova.com
