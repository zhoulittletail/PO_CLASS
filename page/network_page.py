from selenium.webdriver.common.by import By
from base import BaseAction


class NetwrokPage(BaseAction):

    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def click_more(self):
        self.click(self.more_button)

    def click_mobile_network(self):
        self.click(self.mobile_network_button)

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_2g_network(self):
        self.click(self.network_2g_button)

    def click_3g_network(self):
        self.click(self.network_3g_button)
