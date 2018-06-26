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
        self.click(self.more_button)

    def click_mobile_network(self):
        self.click(self.mobile_network_button)

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_2g_network(self):
        self.click(self.network_2g_button)

    def click_3g_network(self):
        self.click(self.network_3g_button)

    def click(self, feature):
        """
        根据某个特征，进行查找并且点击
        :param feature: 特征
        :return:
        """
        self.find_element(feature).click()

    def input(self, feature, text):
        """
        根据某个特征，进行查找并且输入对应的文字
        :param feature: 特征
        :param text: 文字
        :return:
        """
        self.find_element(feature).send_keys(text)

    def find_element(self, feature):
        """
        根据特征，找元素
        :param feature: 特征
        :return: 元素
        """
        return self.driver.find_element(feature[0], feature[1])
