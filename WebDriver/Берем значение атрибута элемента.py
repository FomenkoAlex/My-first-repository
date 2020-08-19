from selenium import webdriver
import time
import math

try:
    link1 = "http://suninjuly.github.io/get_attribute.html"  # определяем переменную с ссылкой
    browser = webdriver.Chrome()
    browser.get(link1)

    img = browser.find_element_by_id("treasure")  # находим елемент
    x = img.get_attribute("valuex")  # кладем в переменную значение атрибута

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    input1 = browser.find_element_by_id("answer")  # находим поле с вводом текста
    input1.send_keys(y)  # вводим ответ в найденое поле
    option1 = browser.find_element_by_id("robotCheckbox")  # находим нужный чекбокс на странице
    option1.click()  # отмечаем галочкой чекбокс
    option = browser.find_element_by_id("robotsRule")  # находим нужный радиобаттон на странице
    option.click()  # кликаем по радиобаттону

    button = browser.find_element_by_css_selector("button.btn")  # находим кнопку
    button.click()  # нажимаем на кнопку


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
