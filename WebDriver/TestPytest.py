import pytest
from selenium import webdriver
import time

def ptest_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")  # находим поле для ввода текста
    input1.send_keys("TestName")  # вводим текст
    input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")  # находим поле для ввода текста
    input2.send_keys("TestLastName")  # вводим текст
    input3= browser.find_element_by_css_selector("input[placeholder='Input your email']")  # находим поле для ввода текста
    input3.send_keys("Test@mail.com")  # вводим текст
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

def ptest_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")  # находим поле для ввода текста
    input1.send_keys("TestName")  # вводим текст
    input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")  # находим поле для ввода текста
    input2.send_keys("TestLastName")  # вводим текст
    input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")  # находим поле для ввода текста
    input3.send_keys("Test@mail.com")  # вводим текст
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == "Congratulations! You have successfully registered!"
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
