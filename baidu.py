from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'platformVersion': '6.0',
    # 　 将要测试app的安装包放到自己电脑上执行安装或启动，如果不是从安装开始，则不是必填项，可以由下面红色的两句直接启动
    'app': 'E:\\package\\com.baidu.searchbox.apk',
    'appPackage': 'com.baidu.searchbox',  # 红色部分如何获取下面讲解
    'appActivity': 'MainActivity',
    'unicodeKeyboard': True,  # 此两行是为了解决字符输入不正确的问题
    'resetKeyboard': True  # 运行完成后重置软键盘的状态　　
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.baidu.searchbox:id/baidu_searchbox").click()
driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput").clear()
driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput").send_keys('appium测试')

driver.find_element_by_id("float_search_or_cancel").click()
driver.find_element_by_id("floating_action_button").click()

driver.quit()
