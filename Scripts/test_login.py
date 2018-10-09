import allure
import pytest

from Base.get_driver import get_driver
from Base.read_yaml import ReadYaml
from Page.page_in import PageIn


def get_data():
    datas=ReadYaml("login.yaml").read_yaml()
    arrs=[]
    for data in datas.values():
        arrs.append((data.get("username"),data.get("password"),data.get("expect"),data.get("toast_expect")))
        return arrs

class TestLogin():
    def setup_class(self):
        #实例化 登陆页面类
        self.login=PageIn(get_driver()).page_get_login()
        #点击我
        self.login.page_click_me()
        #点击已有账户去登陆
        self.login.page_click_info()
    def teardown_class(self):
        #退出driver驱动
        self.login.driver.quit()
    @pytest.mark.parametrize("username,password,expect,toast_expect",get_data())
    def test_login(self,username,password,expect,toast_expect):
        if expect:
            try:
                #输入用户名
                self.login.page_input_user(username)
                #输入密码
                self.login.page_input_pwd(password)
                #点击登陆
                self.login.page_click_login_btn()
                #断言昵称
                assert expect in self.login.page_get_nickname()
                #退出操作
                self.login.page_login_logout()
                #点击我
                self.login.page_click_me()
                #点击已有账户，去登录
                self.login.page_input_info()
            except:
                #截图
                self.login.base_getImage()
                with open("./Image/faild.png","rb")as f:
                    allure.attach("失败描述：",f.read(),allure.attach_type.PNG)
                    allure.attach("描述：","登陆失败！")
                #跑出异常
                raise
            else:
                try:
                    #输入用户名
                    self.login.page_input_user(username)
                    #输入密码
                    self.login.page_input_pwd(password)
                    #点击登陆
                    self.login.page_click_login_btn()
                    #断言toast消息
                    assert toast_expect in self.login.base_get_toast(toast_expect)
                except:
                    #截屏
                    self.login.base_getImage()
                    with open("./Image/faild.png","rb")as f:
                        allure.attach("失败描述：",f.read(),allure.attach_type.PNG)
                        allure.attach("描述：","登陆失败")
                    #抛出异常
                    raise



