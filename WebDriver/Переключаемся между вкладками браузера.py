from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"  # создаем ссылку

try:
    browser = webdriver.Chrome()  # открываем браузер
    browser.get(link)  # переходим по ссылке
    button = browser.find_element_by_css_selector("button.btn")  # находим кнопку
    button.click()  # жмем кнопку
    all_list = browser.window_handles  # получаем список всех вкладок
    new_window = browser.window_handles[1]  # кладем в переменную вторую вкладку
    browser.switch_to.window(new_window)  # переходим по нужной вкладке
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
