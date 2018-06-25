from base import init_driver

class TestDisplay:

    def setup(self):
        self.driver = init_driver()

    def test_display_search(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
