from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"  # создаем ссылку

try:
    browser = webdriver.Chrome()  # открываем браузер
    browser.get(link)  # переходим по ссылке
    button = browser.find_element_by_css_selector("button.btn")  # находим кнопку
    button.click()  # жмем кнопку
    confirm = browser.switch_to.alert  # переключаемся на выскакивающее окно
    confirm.accept()  # жмем в окошке "ОК" с помошью метода (.accept)
    value_x = browser.find_element_by_id("input_value")  # находим нужный елемент
    x = value_x.text  # кладем текст елемента в переменную

    def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))  # создаем функцию

    y = calc(x)  # вызываем функцию с параметрами "х" в котором лежит значение елемента
    input1 = browser.find_element_by_id("answer")  # находим поле с вводом текста
    input1.send_keys(y)  # вводим результат функции в найденое поле, результат хранится в переменной "у"
    button = browser.find_element_by_css_selector("button.btn")  # находим кнопку
    button.click()  # жмем кнопку
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
