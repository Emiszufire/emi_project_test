from playwright.sync_api import expect


class TestMainPage:
    def test_page_has_title(self, open_main_url, page):
        expect(page).to_have_title("DEMOQA")


class TestTextBox:
    def test_name(self, get_textbox_locators):
        actual = get_textbox_locators.get('name')
        expected = "Name:John Doe"
        expect(actual).to_have_text(expected)

    def test_email(self, get_textbox_locators):
        actual = get_textbox_locators.get('email')
        expected = "Email:john@doe.com"
        expect(actual).to_have_text(expected)

    def test_current_address(self, get_textbox_locators):
        actual = get_textbox_locators.get('current_address').all_text_contents()[1]
        expected = "Current Address :Anytown, ST 12345, USA."
        assert actual == expected, f"Actual value '{actual}' does not match expected value '{expected}'"

    def test_permanent_address(self, get_textbox_locators):
        actual = get_textbox_locators.get('permanent_address').all_text_contents()[1]
        expected = "Permanent Address:Sometown, ST 12345, USA."
        assert actual == expected, f"Actual value '{actual}' does not match expected value '{expected}'"

class TestRadioButton:
    def test_yes_visible(self, open_radiobutton_url, page):
        locator = page.get_by_role(role='radio', name='Yes')
        expect(locator).to_be_visible()

    def test_impressive_visible(self, open_radiobutton_url, page):
        locator = page.get_by_role(role='radio', name='Impressive')
        expect(locator).to_be_visible()

    def test_no_visible(self, open_radiobutton_url, page):
        locator = page.get_by_role(role='radio', name='No')
        expect(locator).to_be_visible()

    def test_yes_enable(self, open_radiobutton_url, page):
        locator = page.get_by_role(role='radio', name='Yes')
        expect(locator).to_be_enabled()

    def test_impressive_enable(self, open_radiobutton_url, page):
        locator = page.get_by_role(role='radio', name='Impressive')
        expect(locator).to_be_enabled()

    def test_no_enable(self, open_radiobutton_url, page):
        locator = page.get_by_role(role='radio', name='No')
        expect(locator).to_be_enabled()