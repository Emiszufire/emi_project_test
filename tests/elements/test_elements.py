from playwright.sync_api import expect
from tests.conftest import highlight

class TestMainPage:
    def test_page_has_title(self, open_main_url, page):
        expect(page).to_have_title("DEMOQA")


class TestTextBox:
    def test_name(self, get_textbox_locators):
        actual = get_textbox_locators.get('name')
        highlight(actual)
        expected = "Name:John Doe"
        expect(actual).to_have_text(expected)

    def test_email(self, get_textbox_locators):
        actual = get_textbox_locators.get('email')
        highlight(actual)
        expected = "Email:john@doe.com"
        expect(actual).to_have_text(expected)

    def test_current_address(self, get_textbox_locators):
        actual = get_textbox_locators.get('current_address')
        highlight(actual)
        expected = "Current Address :Anytown, ST 12345, USA."
        expect(actual).to_have_text(expected)

    def test_permanent_address(self, get_textbox_locators):
        actual = get_textbox_locators.get('permanent_address')
        highlight(actual)
        expected = "Permanent Address:Sometown, ST 12345, USA."
        expect(actual).to_have_text(expected)


class TestTextBoxWithoutEmail:
    def test_name_without_email(self, get_textbox_locators_without_email):
        actual = get_textbox_locators_without_email.get('name')
        highlight(actual)
        expected = "Name:John Doe"
        expect(actual).to_have_text(expected)

    def test_email_attached_without_email(self, get_textbox_locators_without_email):
        actual = get_textbox_locators_without_email.get('email')
        # highlight(actual)
        expect(actual).not_to_be_attached()

    def test_current_address_without_email(self, get_textbox_locators_without_email):
        actual = get_textbox_locators_without_email.get('current_address')
        highlight(actual)
        expected = "Current Address :Anytown, ST 12345, USA."
        expect(actual).to_have_text(expected)

    def test_permanent_address_without_email(self, get_textbox_locators_without_email):
        actual = get_textbox_locators_without_email.get('permanent_address')
        highlight(actual)
        expected = "Permanent Address:Sometown, ST 12345, USA."
        expect(actual).to_have_text(expected)

class TestTextBoxWrongEmailOne:
    def test_name_wrong_email_one(self, get_textbox_locators_wrong_email_one):
        actual = get_textbox_locators_wrong_email_one.get('name')
        expect(actual).not_to_be_visible()

    def test_email_wrong_email_one(self, get_textbox_locators_wrong_email_one):
        actual = get_textbox_locators_wrong_email_one.get('email')
        expect(actual).not_to_be_visible()

    def test_current_address_wrong_email_one(self, get_textbox_locators_wrong_email_one):
        actual = get_textbox_locators_wrong_email_one.get('current_address')
        highlight(actual)
        expect(actual).not_to_be_visible()

    def test_permanent_address_wrong_email_one(self, get_textbox_locators_wrong_email_one):
        actual = get_textbox_locators_wrong_email_one.get('permanent_address').all_text_contents()[1]
        expect(actual).not_to_be_visible()

class TestTextBoxWrongEmailTwo:
    def test_name_wrong_email_two(self, get_textbox_locators_wrong_email_two):
        actual = get_textbox_locators_wrong_email_two.get('name')
        expect(actual).not_to_be_visible()

    def test_email_wrong_email_two(self, get_textbox_locators_wrong_email_two):
        actual = get_textbox_locators_wrong_email_two.get('email')
        expect(actual).not_to_be_visible()

    def test_current_address_wrong_email_two(self, get_textbox_locators_wrong_email_two):
        actual = get_textbox_locators_wrong_email_two.get('current_address').all_text_contents()[1]
        expect(actual).not_to_be_visible()

    def test_permanent_address_wrong_email_two(self, get_textbox_locators_wrong_email_two):
        actual = get_textbox_locators_wrong_email_two.get('permanent_address').all_text_contents()[1]
        expect(actual).not_to_be_visible()

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
        no_radio_locator = page.locator('#noRadio')
        expect(no_radio_locator).not_to_be_checked()
