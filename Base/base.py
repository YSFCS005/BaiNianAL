from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver=driver
    #查找元素
    def base_find_element(self,loc):
        return WebDriverWait(self.driver,timeout=30,poll_frequency=0.5).until(lambda x:x.find_element(*loc))
    #点击
    def base_click(self,loc):
        #调用自己封装查找元素类
        self.base_find_element(loc)
    #输入
    def base_input(self,loc,text):
        el=self.base_find_element(loc)
        #输入内容之前先清楚操作 不会影响整体输入效果
        el.clear()
        #输入内容
        el.send_keys(text)

    #截屏
    def base_getImage(self):
        Path="./Image/faild.png"
        self.driver.get_screenshort_as_file(Path)
    #获取toast消息
    def base_get_toast(self,message):
        #组装 定位目标元素语法
        return self.base_xpath(message).text
    #xpath 文本模糊定位封装
    def base_xpath(self,text):
        """
        :param text: 传入要查找的文件
        :return: 元素
        """
        loc=By.XPATH,"//*[contains(@text,'"+text+"')]"
        return self.base_find_element(loc)
    #滑动元素封装
    def base_drag_and_drop(self,el1,el2):
        """
        :param el1: 要开始滑动的元素
        :param el2: 把元素滑动到指定元素
        """
        self.driver.drag_and_drop(el1,el2)
    #获取文本方法
    def base_get_text(self,loc):
        return self.base_find_element(loc).text

