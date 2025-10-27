"""
https://stepik.org/course/575/syllabus
"""

# Импорт модулей
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"  # Ссылка на страницу

# Инициализация драйвера и открытие браузера
try:
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 10)   # Ожидание появления элементов

    # Производим поиск элемента и вводим данные в поле формы
    input1 = wait.until(EC.presence_of_element_located((By.NAME, 'first_name')))
    input1.send_keys('Danil')
    """
    EC.presence_of_element_located: Условие, которое проверяет наличие элемента на странице.
    By.NAME: Указывает, что элемент будет найден по атрибуту name.
    input1.send_keys('Ivan'): Вводит текст 'Ivan' в найденное поле.
    """
    input2 = wait.until(EC.presence_of_element_located((By.NAME, 'last_name')))
    input2.send_keys('Shevchenko')

    input3 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control.city')))
    input3.send_keys('Rostov-on-Don')

    input4 = wait.until(EC.presence_of_element_located((By.ID, 'country')))
    input4.send_keys('Russia')
    """
    EC.element_to_be_clickable: Условие, которое проверяет, что элемент доступен для клика.
    By.CSS_SELECTOR: Указывает, что элемент будет найден по CSS-селектору.
    button.click(): Нажимает на найденную кнопку.
    """

    # Производим нажатие на кнопку
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn')))
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(15)
    # Закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла