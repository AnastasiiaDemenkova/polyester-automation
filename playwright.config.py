import os

# Failures-only artifact storage for pytest-playwright
def pytest_playwright_capture_artifacts(config):
    return "only-on-failure"

# Configure artifact directory
def pytest_configure(config):
    os.environ["PLAYWRIGHT_ARTIFACTS"] = "playwright-artifacts"
