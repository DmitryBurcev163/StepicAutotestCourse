from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
button.click()

#переключаемся на вновь открыую вкладку
new_window = browser.window_handles[1] #нумерация вкладок начинается с 0, т.е первая вкладка будет иметь значеие =[0]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value").text
x = x_element
y = calc(x)

try:
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
	button = browser.find_element_by_css_selector("button.btn.btn-primary")
	button.click()



finally:
	# успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

