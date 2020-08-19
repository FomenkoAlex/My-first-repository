from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"  # создаем ссылку

try:
    browser = webdriver.Chrome()  # открываем браузер
    browser.get(link)  # переходим по ссылке
    input1 = browser.find_element_by_name("firstname")  # находим поле для ввода текста
    input1.send_keys("TestName")  # вводим текст
    input2 = browser.find_element_by_name("lastname")  # находим поле для ввода текста
    input2.send_keys("TestLastName")  # вводим текст
    input3 = browser.find_element_by_name("email")  # находим поле для ввода текста
    input3.send_keys("Test@mail.com")  # вводим текст
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'TestDoc.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_css_selector("input[type='file']")  # находим елемент который позволяет загрузить файл
    element.send_keys(file_path)  # загружаем файл
    button = browser.find_element_by_css_selector("button.btn")  # находим кнопку
    button.click()  # жмем кнопку
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
