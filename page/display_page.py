class DisplayPage:

    def __init__(self, driver):
        self.driver = driver

    def click_display(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()

    def click_search(self):
        self.driver.find_element_by_id("com.android.settings:id/search").click()

    def input_keyword(self, content):
        self.driver.find_element_by_id("android:id/search_src_text").send_keys(content)

    def click_back(self):
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
