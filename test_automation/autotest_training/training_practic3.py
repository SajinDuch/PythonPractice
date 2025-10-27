"""
https://stepik.org/course/575/syllabus
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
#💡Поиск элементов по CSS_SELECTOR:
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Используем CSS selector для всех полей на странице с типом "text"
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")

    #  Проходим цикл по каждому полю и записываем туда тестовые данные
    for element in elements:
        element.send_keys("Мой ответ")

    # Нажимаем кнопку submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Дожидаемся результата (30 секунд)
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

    '''

"""
#💡 Поиск элементов по XPath:
     Для поиска всех текстовых полей по XPath мы написали следующий путь://input[@type='text']
     Здесь:
        //input: находим все элементы input.
        @type='text': выбираем только те элементы, у которых атрибут type имеет значение "text".
"""
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Поиск всех текстовых полей на странице с помощью xpath
    elements = browser.find_elements(By.XPATH, "//input[@type='text']")

    # Заполняем каждое поле
    for element in elements:
        element.send_keys("Мой ответ")

    # Новая попытка найти кнопку
    button = browser.find_element(By.XPATH, "//button[contains(@class,'btn')]")
    button.click()

finally:
    # Дожидаемся результата (30 секунд)
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

    """
    Иногда лучше проверять наличие кнопок по альтернативному признаку, например, по её названию:
        button = browser.find_element(By.XPATH, "//button[.='Submit']")

    Или с учётом вложенности элементов:
        button = browser.find_element(By.XPATH, "//div/button[@class='btn']")
    """