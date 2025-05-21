import os

import pytest
import pytest_html
from playwright.sync_api import sync_playwright
from pytest_metadata.plugin import metadata_key
from datetime import datetime, timezone
import getpass
from PIL import ImageGrab


def pytest_configure(config):
    config.stash[metadata_key]["designer"] = "Tester"
    config.stash[metadata_key]["datetime"] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %z')
    config.stash[metadata_key]["user"] = getpass.getuser()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        # # Always add a URL to the report
        # extras.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # # Add custom HTML
            # extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            # Take and attach a screenshot
            try:
                screenshots_dir = "screenshots"
                os.makedirs(screenshots_dir, exist_ok=True)
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"{item.name}_{timestamp}.png"
                filepath = os.path.join(screenshots_dir, filename)
                ImageGrab.grab().save(filepath)
                extras.append(pytest_html.extras.image(filepath))
            except Exception as e:
                print(f"Screenshot failed: {e}")

        report.extras = extras


@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("--browser")[0]
    headed = request.config.getoption("--headed")
    slow_mo = request.config.getoption("--slowmo")
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=not (headed), slow_mo=slow_mo, args=["--start-maximized"])
        request.config.stash[metadata_key]["browser"] = f'{browser.browser_type.name} {browser.version}'
        request.config.stash[metadata_key]["browser headed"] = headed
        request.config.stash[metadata_key]["browser slow motion"] = slow_mo
        yield browser
        browser.close()


@pytest.fixture(scope="module")
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
def open_slider_url(page):
    page.goto("https://demoqa.com/slider")
