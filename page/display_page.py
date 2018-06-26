from selenium.webdriver.common.by import By


class DisplayPage:

    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        self.driver = driver

    def click_display(self):
        self.click(self.display_button)

    def click_search(self):
        self.click(self.search_button)

    def input_keyword(self, content):
        self.input(self.search_edit_text, content)

    def click_back(self):
        self.click(self.back_button)

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
