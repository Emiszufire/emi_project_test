import pytest


# @pytest.fixture
# def move_slider(page):
#     def move(value):
#         page.get_by_role("slider").fill(value)
#         return page.locator("#sliderValue")
#     return move

@pytest.fixture(params=["20", "40", "60", "80", "100"], ids=['position_20', 'position_40', 'position_60', 'position_80', 'position_100'])
def move_slider(request, page):
    page.get_by_role("slider").fill(request.param)
    return request.param
