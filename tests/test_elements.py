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

    def test_three_true(self, do_operations_textbox_fullname,do_operations_textbox_nameexamplecom,do_operations_textbox_currentaddress, click_submit, get_textbox_locators, page):
        actual = get_textbox_locators
        expected = "Name:John Doe"
        expect(actual).to_have_text(expected)

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

    def test_yes_checked(self, open_radiobutton_url, page):
        yes_label_locator = page.locator('label[for="yesRadio"]')
        yes_radio_locator = page.locator('#yesRadio')
        expect(yes_radio_locator).not_to_be_checked()
        yes_label_locator.click()
        expect(yes_radio_locator).to_be_checked()

    def test_impressive_checked(self, open_radiobutton_url, page):
        impressive_label_locator = page.locator('label[for="impressiveRadio"]')
        impressive_radio_locator = page.locator('#impressiveRadio')
        expect(impressive_radio_locator).not_to_be_checked()
        impressive_label_locator.click()
        expect(impressive_radio_locator).to_be_checked()

    def test_no_checked(self, open_radiobutton_url, page):
        no_label_locator = page.locator('label[for="noRadio"]')
        no_radio_locator = page.locator('#noRadio')
        expect(no_radio_locator).not_to_be_checked()
    #     no_label_locator.click()
    #     expect(no_radio_locator).to_be_checked()
