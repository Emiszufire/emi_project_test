import pytest
from playwright.sync_api import sync_playwright
from pytest_metadata.plugin import metadata_key
from datetime import datetime, timezone
import getpass

def pytest_configure(config):
    config.stash[metadata_key]["designer"] = "Tester"
    config.stash[metadata_key]["datetime"] = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    config.stash[metadata_key]["datetime"] = str(datetime.now().astimezone(timezone.utc))
    config.stash[metadata_key]["user"] = getpass.getuser()

@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000, args=["--start-maximized"])
        request.config.stash[metadata_key]["browser"] = f'{browser.browser_type.name} {browser.version}'
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()