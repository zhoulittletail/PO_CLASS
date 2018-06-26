from base import init_driver
from page.network_page import NetwrokPage
from page.page import Page


class TestNetwrok:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_network_2g(self):
        self.page.network.click_more()
        self.page.network.click_mobile_network()
        self.page.network.click_first_network()
        self.page.network.click_2g_network()

    def test_network_3g(self):
        self.page.network.click_more()
        self.page.network.click_mobile_network()
        self.page.network.click_first_network()
        self.page.network.click_3g_network()