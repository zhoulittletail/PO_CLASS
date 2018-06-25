from selenium.webdriver.common.by import By


class NetwrokPage:

    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        self.driver = driver

    def click_more(self):
        self.find_element(self.more_button).click()

    def click_mobile_network(self):
        self.find_element(self.mobile_network_button).click()

    def click_first_network(self):
        self.find_element(self.first_network_button).click()

    def click_2g_network(self):
        self.find_element(self.network_2g_button).click()

    def click_3g_network(self):
        self.find_element(self.network_3g_button).click()

    def find_element(self, feature):
        return self.driver.find_element(feature[0], feature[1])
