from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

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
        by = feature[0]
        value = feature[1]
        if by == By.XPATH:
            value = self.__make_xpath_with_feature(value)
            print(value)
        wait = WebDriverWait(self.driver, 5, 1)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self, feature):
        """
        根据特征，找元素
        :param feature: 特征
        :return: 元素
        """
        wait = WebDriverWait(self.driver, 5, 1)
        return wait.until(lambda x: x.find_elements(feature[0], feature[1]))

    @staticmethod
    def __make_xpath_with_unit_feature(loc):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "

        return feature

    def __make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc

            # loc str
            feature = self.__make_xpath_with_unit_feature(loc)
        else:
            # loc 列表
            for i in loc:
                feature += self.__make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and ")

        loc = feature_start + feature + feature_end

        return loc
