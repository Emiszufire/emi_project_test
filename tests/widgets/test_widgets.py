from playwright.sync_api import expect


class TestSlider:
    def test_move_slider(self, open_slider_url, move_slider, page):
        locator = page.locator("#sliderValue")
        position = move_slider
        expect(locator).to_have_value(position)
