import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 创建对象
driver = webdriver.Chrome()
# 加载URL
driver.get("https://www.xin.com/beijing")
time.sleep(3)
# 窗口放大
# driver.maximize_window();
driver.find_element_by_id("MD-home-banner-brandSearch").send_keys("宝马")
time.sleep(3)
# 滑动条
driver.execute_script("window.scrollBy(0,500)")
# 等待几秒
time.sleep(3)
while 1:
    try:
        # 鼠标悬停
        a = driver.find_element_by_xpath(".//ul[@id='ui-id-1']/li[@data-number-index='9']")
        ActionChains(driver).move_to_element(a).perform()
        time.sleep(2)
        # 点击搜索词宝马X3进口
        driver.find_element_by_xpath(".//ul[@id='ui-id-1']/li[@data-number-index='9']").click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,500)")
        time.sleep(2)
        b = driver.find_element_by_xpath(".//*[@id='search_container']/div[1]/ul/li[2]/div[2]/a/div")
        ActionChains(driver).move_to_element(b).perform()
        time.sleep(2)
        # 点击车辆进入车辆详情页
        driver.find_element_by_xpath(".//*[@id='search_container']/div[1]/ul/li[2]/div[2]/a/div").click()
        time.sleep(3)
        print("已定位到元素")
        # 关闭窗口
        driver.quit()
        break
    except:
        wei = "还未定位到元素!"
        if wei.__eq__("还未定位到元素!"):
            # 截屏
            driver.get_screenshot_as_file("优信二手车.png")
            print(wei)
        break
