import pytest
from playwright.sync_api import sync_playwright
from pytest_metadata.plugin import metadata_key
from datetime import datetime, timezone
import getpass


def pytest_configure(config):
    config.stash[metadata_key]["designer"] = "Tester"
    config.stash[metadata_key]["datetime"] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %z')
    config.stash[metadata_key]["user"] = getpass.getuser()


@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("--browser")[0]
    headed = not(request.config.getoption("--headed"))
    slow_mo = request.config.getoption("--slowmo")
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=headed, slow_mo=slow_mo, args=["--start-maximized"])
        request.config.stash[metadata_key]["browser"] = f'{browser.browser_type.name} {browser.version}'
        yield browser
        browser.close()


@pytest.fixture(scope="class")
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page
    context.tracing.stop(path="trace.zip")
    context.close()


@pytest.fixture(scope="class")
def open_main_url(page):
    page.goto("https://demoqa.com/elements")


@pytest.fixture(scope="class")
def open_textbox_url(page):
    page.goto("https://demoqa.com/text-box")

@pytest.fixture(scope="class")
def open_radiobutton_url(page):
    page.goto("https://demoqa.com/radio-button")


@pytest.fixture(scope="class")
def do_operations_textbox(open_textbox_url, page):
    page.get_by_role(role='textbox', name='Full Name').fill("John Doe")
    page.get_by_role(role='textbox', name='name@example.com').fill("john@doe.com")
    page.get_by_role(role='textbox', name='Current Address').fill("Anytown, ST 12345, USA.")
    page.locator('#permanentAddress').fill("Sometown, ST 12345, USA.")

    page.get_by_role(role='button', name='Submit').click()
    page.wait_for_timeout(500)


@pytest.fixture(scope="class")
def get_textbox_locators(do_operations_textbox, page):
    name = page.locator("#name")
    email = page.locator("#email")
    current_address = page.locator("#currentAddress")
    permanent_address = page.locator("#permanentAddress")
    locators = {
        "name": name,
        "email": email,
        "current_address": current_address,
        "permanent_address": permanent_address
    }
    return locators
