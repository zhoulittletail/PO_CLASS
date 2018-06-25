from base import init_driver
from page.network_page import NetwrokPage

class TestNetwrok:

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetwrokPage(self.driver)

    def test_network_2g(self):
        self.network_page.click_more()
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_2g_network()

    def test_network_3g(self):
        self.network_page.click_more()
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_3g_network()