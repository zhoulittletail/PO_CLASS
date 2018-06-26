from page.display_page import DisplayPage
from page.network_page import NetworkPage


class Page:

    # @property
    # 含义就是把一个放大当成一个属性来调用，方法内部也会执行

    def __init__(self, driver):
        self.driver = driver

    @property
    def display(self):
        return DisplayPage(self.driver)

    @property
    def network(self):
        return NetworkPage(self.driver)
