from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 使用无界面Chrome打开网页
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# 定义输入框的输入城市字符
city = input("输入城市：")

# 在浏览器中打开链接
driver.get("http://www.weather.com.cn/")

# 寻找id为txtZip的元素，即输入框
chaxun = driver.find_element_by_id("txtZip")
# 自动输入城市字符
chaxun.send_keys(city)
# 模拟点击查询按钮
button = driver.find_element_by_id("btnZip")
button.click()

# 输出此时的浏览器选项卡
# print(driver.window_handles)
# 延时等待，设置等待时间为5秒
time.sleep(5)
# 输出此时的浏览器选项卡，此时的选项卡数量增加一个，增加的选项卡为查询城市的结果页面
# print(driver.window_handles)
# 浏览器切换至新打开的选项卡
driver.switch_to.window(driver.window_handles[1])

# 获取选项卡链接
url = driver.current_url
print(url)

# 退出浏览器
driver.quit()