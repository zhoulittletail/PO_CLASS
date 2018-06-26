from appium.webdriver.common.touch_action import TouchAction

from base import init_driver
from page import Page


class TestDisplay:

    driver, page = None, None

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        TouchAction

    def test_display_search(self):
        self.page.display.click_display()
        self.page.display.click_search()
        self.page.display.input_keyword("hello")
        self.page.display.click_back()
