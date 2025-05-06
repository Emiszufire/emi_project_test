from playwright.sync_api import expect


class TestMainPage:
    def test_page_has_title(self, page):
        page.goto("https://demoqa.com/elements")
        expect(page).to_have_title("DEMOQA")
