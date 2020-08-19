from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"  # создаем ссылку

try:
    browser = webdriver.Chrome()  # открываем браузер
    browser.get(link)  # переходим по ссылке
    value_x = browser.find_element_by_id("input_value")
    x = value_x.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    inputs = browser.find_element_by_tag_name("input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", inputs)
    inputs.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")  # находим нужный чекбокс на странице
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()  # отмечаем галочкой чекбокс
    radiobutton = browser.find_element_by_id("robotsRule")  # находим нужный радиобаттон на странице
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()  # кликаем по радиобаттону
    button = browser.find_element_by_css_selector("button.btn")  # находим кнопку
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()  # жмем кнопку
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
