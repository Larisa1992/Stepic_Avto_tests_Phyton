from selenium import webdriver
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element_by_css_selector(".trollface")
button.click()

#Имя новой вкладки
new_window = browser.window_handles[1]

print("window_handles[1] = ",new_window)

#Для переключения на новую вкладку
browser.switch_to.window(new_window)

element = browser.find_element_by_id("input_value")
x = int(element.text)


inp = browser.find_element_by_id("answer")
inp.send_keys(str(calc(x)))


button = browser.find_element_by_css_selector(".btn")
button.click()
