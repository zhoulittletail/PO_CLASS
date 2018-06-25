class NetwrokPage:

    def __init__(self, driver):
        self.driver = driver

    def click_more(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()

    def click_mobile_network(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()

    def click_first_network(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()

    def click_2g_network(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def click_3g_network(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()