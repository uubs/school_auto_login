#!/usr/bin/env python3
from selenium import webdriver

########################## user info #################################
Username = "20S103141"
Password = "Pi3.141592653"

# configure web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # no windows argument
chrome_options.add_argument('--disable-gpu') # need to be added
browser = webdriver.Chrome(options=chrome_options, executable_path=r'/home/huang/chromedriver')
browser.set_window_position(0, 0)
browser.set_window_size(1800, 700)


# find login input page
browser.get("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/shsj/loginChange")
browser.find_element_by_xpath('/html/body/div[1]/div[2]/button[1]').click()

# change window to the newly opened window
browser.switch_to.window(browser.window_handles[-1])

# input username and password
browser.find_element_by_xpath('//*[@id="username"]').clear()
browser.find_element_by_xpath('//*[@id="username"]').send_keys(Username)
browser.find_element_by_xpath('//*[@id="password"]').clear()
browser.find_element_by_xpath('//*[@id="password"]').send_keys(Password) #password
# click login in
browser.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()

# change window to the newly opened window
browser.switch_to.window(browser.window_handles[-1])

# goto 每日上报
browser.find_element_by_xpath('//*[@id="mrsb"]').click()

# change window to the newly opened window
browser.switch_to.window(browser.window_handles[-1])

# 新增
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/a/div').click()

print("success");
