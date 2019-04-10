# 导入webdriver
from selenium import webdriver
#要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time

# 定义输入框的输入城市字符
city = input("输入城市：")

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()
# 设置窗体大小
driver.set_window_size(1366, 768)

# 在PhantomJS打开链接
driver.get("http://www.weather.com.cn/")

# 寻找id为txtZip的元素，即输入框
chaxun = driver.find_element_by_id("txtZip")
# 自动输入城市字符
chaxun.send_keys(city)
# 模拟点击查询按钮
button = driver.find_element_by_id("btnZip")
button.click()

# 输出此时的浏览器选项卡
print(driver.window_handles)
# 延时等待，设置等待时间为5秒
time.sleep(5)
# 输出此时的浏览器选项卡，此时的选项卡数量增加一个，增加的选项卡为查询城市的结果页面
print(driver.window_handles)
# 浏览器切换至新打开的选项卡
driver.switch_to.window(driver.window_handles[1])

# 获取选项卡链接
url = driver.current_url
print(url)

# 退出浏览器
driver.quit()


# driver = webdriver.Chrome()
# driver.set_window_size(1366, 768)
# driver.get("http://www.baidu.com/")
# button = driver.find_element_by_partial_link_text("hao123")
# button.click()
# print(driver.window_handles)
# time.sleep(5)
# html = driver.current_url
# driver.quit()
# print(html)

# -*-  coding:utf-8 -*-
# 主要用来测试selenium使用phantomJs

# # 导入webdriver
# from selenium import webdriver
# import time

# #要想调用键盘按键操作需要引入keys包
# from selenium.webdriver.common.keys import Keys

# #调用环境变量指定的PhantomJS浏览器创建浏览器对象
# driver = webdriver.PhantomJS()
# driver.set_window_size(1366, 768)
# #如果没有在环境变量指定PhantomJS位置
# #driver = webdriver.PhantomJS(executable_path = "./phantomjs")

# #get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)

# driver.get("http://www.baidu.com/")

# #获取页面名为wraper的id标签的文本内容
# data = driver.find_element_by_id('wrapper').text

# #打印数据内容
# print(data)

# print(driver.title)

# #生成页面快照并保存
# # driver.save_screenshot("baidu.png")

# # id="kw"是百度搜索输入框，输入字符串"长城"
# driver.find_element_by_id('kw').send_keys(u'长城')

# # id="su"是百度搜索按钮，click()是模拟点击
# driver.find_element_by_id('su').click()

# #获取新的页面快照
# # driver.save_screenshot("长城.png")

# #打印网页渲染后的源代码
# print(driver.page_source)

# #获取当前页面Cookie
# print(driver.get_cookies())

# #ctrl+a全选输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# #ctrl+x剪切输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

# #输入框重新输入内容
# driver.find_element_by_id('kw').send_keys('itcast')

# #模拟Enter回车键
# driver.find_element_by_id('su').send_keys(Keys.RETURN)
# time.sleep(5)

# #清空输入框内容
# driver.find_element_by_id('kw').clear()

# #生成新的页面快照
# # driver.save_screenshot('itcast.png')

# #获取当前url
# print(driver.current_url)

# driver.quit()