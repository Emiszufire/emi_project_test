import pytest


@pytest.fixture(params=["20", "40", "60", "80", "100"], ids=['position_20', 'position_40', 'position_60', 'position_80', 'position_100'])
def move_slider(request, page, open_slider_url):
    page.get_by_role("slider").fill(request.param)
    return request.param


@pytest.fixture(scope="class")
def open_accordian_first(page):
    page.get_by_text("What is Lorem Ipsum?").click()


@pytest.fixture(scope="class")
def open_accordian_second(page):
    page.get_by_text("Where does it come from?").click()


@pytest.fixture(scope="class")
def open_accordian_third(page):
    page.get_by_text("Why do we use it?").click()
