from selenium.webdriver.common.by import By


class DisplayPage:

    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        self.driver = driver

    def click_display(self):
        self.find_element(self.display_button).click()

    def click_search(self):
        self.find_element(self.search_button).click()

    def input_keyword(self, content):
        self.find_element(self.search_edit_text).send_keys(content)

    def click_back(self):
        self.find_element(self.back_button).click()

    def find_element(self, feature):
        return self.driver.find_element(feature[0], feature[1])
