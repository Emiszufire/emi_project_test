from playwright.sync_api import expect


class TestSlider:
    def test_move_slider(self, move_slider, page):
        locator = page.locator("#sliderValue")
        position = move_slider
        expect(locator).to_have_value(position)


class TestAccordian:
    def test_accordian_visible_panel1(self, open_accordian_url, page):
        locator = page.locator("#section1Content")
        expect(locator).to_be_visible()

    def test_accordian_change_visible_panel1(self, page, open_accordian_first):
        locator = page.locator("#section1Content")
        expect(locator).not_to_be_visible()

    def test_change_accordian_panel2(self, page, open_accordian_second):
        locator = page.locator("#section2Content")
        expect(locator).to_contain_text("Contrary to popular belief")

    def test_change_accordian_panel3(self, page, open_accordian_third):
        locator = page.locator("#section3Content")
        expect(locator).to_contain_text("It is a long established")
