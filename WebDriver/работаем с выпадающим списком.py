from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"  # создаем ссылку

try:
    browser = webdriver.Chrome()  # открываем браузер
    browser.get(link)  # переходим по ссылке
    num1 = browser.find_element_by_id("num1")  # находим нужный елемент, в данном случае это число
    a = num1.text  # кладем в переменную первое число
    num2 = browser.find_element_by_id("num2")  # находим второе нужное число
    b = num2.text  # также кладем в переменную
    x = int(a) + int(b)  # суммируем числа,сразу же преобразовуя из строки в число

    select = Select(browser.find_element_by_tag_name("select"))  # находим выпадающий список на странице
    select.select_by_visible_text(str(x))  # из списка выбираем то значение которое получилось ранее, сразу же
                                           # преобразовуя в число
    button = browser.find_element_by_css_selector("button.btn")  # находим кнопку
    button.click()  # жмем кнопку
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
