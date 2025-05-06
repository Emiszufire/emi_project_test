import pytest
from playwright.sync_api import sync_playwright
from pytest_metadata.plugin import metadata_key
from datetime import datetime


def pytest_configure(config):
    config.stash[metadata_key]["designer"] = "Tester"
    config.stash[metadata_key]["datetime"] = str(datetime.now())

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=5000, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()