from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    time.sleep(1)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_element.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    # browser.quit()


# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/redirect_accept.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#     time.sleep(1)
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     y = calc(x)
#     y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
#     y_element.send_keys(y)
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/alert_accept.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#     time.sleep(1)
#     alert = browser.switch_to.alert
#     alert.accept()
#     # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     y = calc(x)
#     y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
#     y_element.send_keys(y)
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()



# import math
# import os
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "https://suninjuly.github.io/file_input.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
#     first_name.send_keys("Harry")
#     last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
#     last_name.send_keys("Potter")
#     email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
#     email.send_keys("hp@hogwarts.edu")
#     f = browser.find_element(By.CSS_SELECTOR, "#file")
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#
#     f.send_keys(os.path.join(current_dir, "123.txt"))
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "https://SunInJuly.github.io/execute_script.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     y = calc(x)
#     y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
#     y_element.send_keys(y)
#     option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     option1.click()
#     browser.execute_script("window.scrollBy(0, 80);")
#     option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     option2.click()
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# time.sleep(2)
# button = browser.find_element(By.TAG_NAME, "button")
# # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# browser.execute_script("window.scrollBy(0, 100);")
#
# time.sleep(5)
# button.click()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# link = "https://suninjuly.github.io/selects1.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
#     num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(str(int(num1) + int(num2)))
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# # link = "https://suninjuly.github.io/math.html"
# link = "http://suninjuly.github.io/get_attribute.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
#     x = x_element.get_attribute("valuex")
#     y = calc(x)
#     y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
#     y_element.send_keys(y)
#     option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     option1.click()
#     option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     option2.click()
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link ="http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
#     link.click()
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(90)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# 1.6.4

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла