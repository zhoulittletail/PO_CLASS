from base import init_driver
from page.display_page import DisplayPage

class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_display_search(self):
        self.display_page.click_display()
        self.display_page.click_search()
        self.display_page.input_keyword()
        self.display_page.click_back()

    # def test_display_search1(self):
    #     self.display_page.click_search()
    #     self.display_page.input_keyword()
    #     self.display_page.click_back()