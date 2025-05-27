import pytest


@pytest.fixture(scope="class")
def do_operations_textbox(open_textbox_url, page):
    page.get_by_role(role='textbox', name='Full Name').fill("John Doe")
    page.get_by_role(role='textbox', name='name@example.com').fill("john@doe.com")
    page.get_by_role(role='textbox', name='Current Address').fill("Anytown, ST 12345, USA.")
    page.locator('#permanentAddress').fill("Sometown, ST 12345, USA.")


@pytest.fixture(scope="class")
def do_operations_textbox_wrong_email_one(open_textbox_url, page):
    page.get_by_role(role='textbox', name='Full Name').fill("John Doe")
    page.get_by_role(role='textbox', name='name@example.com').fill("johndoe.com")
    page.get_by_role(role='textbox', name='Current Address').fill("Anytown, ST 12345, SA.")
    page.locator('#permanentAddress').fill("Sometown, ST 12345, USA.")


@pytest.fixture(scope="class")
def do_operations_textbox_wrong_email_two(open_textbox_url, page):
    page.get_by_role(role='textbox', name='Full Name').fill("John Doe")
    page.get_by_role(role='textbox', name='name@example.com').fill("john@doecom")
    page.get_by_role(role='textbox', name='Current Address').fill("Anytown, ST 12345, SA.")
    page.locator('#permanentAddress').fill("Sometown, ST 12345, USA.")


@pytest.fixture(scope="class")
def do_operations_textbox_without_email(open_textbox_url, page):
    page.get_by_role(role='textbox', name='Full Name').fill("John Doe")
    page.get_by_role(role='textbox', name='Current Address').fill("Anytown, ST 12345, SA.")
    page.locator('#permanentAddress').fill("Sometown, ST 12345, USA.")


@pytest.fixture(scope="class")
def click_submit(page):
    page.get_by_role(role='button', name='Submit').click()
    page.wait_for_timeout(500)


# @pytest.fixture(scope="class")
# def do_operations_textbox_fullname(open_textbox_url, page):
#     page.get_by_role(role='textbox', name='Full Name').fill("John Doe")
#
#
# @pytest.fixture(scope="class")
# def do_operations_textbox_nameexamplecom(open_textbox_url, page):
#     page.get_by_role(role='textbox', name='name@example.com').fill("john@doe.com")
#
#
# @pytest.fixture(scope="class")
# def do_operations_textbox_nameexamplecommiastake1(open_textbox_url, page):
#     page.get_by_role(role='textbox', name='name@example.com').fill("johndoe.com")
#
#
# @pytest.fixture(scope="class")
# def do_operations_textbox_nameexamplecommiastake2(open_textbox_url, page):
#     page.get_by_role(role='textbox', name='name@example.com').fill("john@doecom")
#
#
# @pytest.fixture(scope="class")
# def do_operations_textbox_currentaddress(open_textbox_url, page):
#     page.get_by_role(role='textbox', name='Current Address').fill("Anytown, ST 12345, USA.")
#
#
# @pytest.fixture(scope="class")
# def do_operations_textbox_permanentaddress(open_textbox_url, page):
#     page.locator('#permanentAddress').fill("Sometown, ST 12345, USA.")


@pytest.fixture(scope="class")
def get_textbox_locators(do_operations_textbox, click_submit, page):
    name = page.locator("#name.mb-1")
    email = page.locator("#email.mb-1")
    current_address = page.locator("#currentAddress.mb-1")
    permanent_address = page.locator("#permanentAddress.mb-1")
    locators = {
        "name": name,
        "email": email,
        "current_address": current_address,
        "permanent_address": permanent_address
    }
    return locators

@pytest.fixture(scope="class")
def get_textbox_locators_without_email(do_operations_textbox_without_email, click_submit, page):
    name = page.locator("#name.mb-1")
    email = page.locator("#email.mb-1")
    current_address = page.locator("#currentAddress.mb-1")
    permanent_address = page.locator("#permanentAddress.mb-1")
    locators = {
        "name": name,
        "email": email,
        "current_address": current_address,
        "permanent_address": permanent_address
    }
    return locators

@pytest.fixture(scope="class")
def get_textbox_locators_wrong_email_one(do_operations_textbox_wrong_email_one, click_submit, page):
    name = page.locator("#name.mb-1")
    email = page.locator("#email.mb-1")
    current_address = page.locator("#currentAddress.mb-1")
    permanent_address = page.locator("#permanentAddress.mb-1")
    locators = {
        "name": name,
        "email": email,
        "current_address": current_address,
        "permanent_address": permanent_address
    }
    return locators

@pytest.fixture(scope="class")
def get_textbox_locators_wrong_email_two(do_operations_textbox_wrong_email_two, click_submit, page):
    name = page.locator("#name.mb-1")
    email = page.locator("#email.mb-1")
    current_address = page.locator("#currentAddress.mb-1")
    permanent_address = page.locator("#permanentAddress.mb-1")
    locators = {
        "name": name,
        "email": email,
        "current_address": current_address,
        "permanent_address": permanent_address
    }
    return locators
#
#
#

