"""
https://stepik.org/course/575/syllabus

---✍️ ЗАДАНИЕ: Stepik
    Ваша программа должна выполнить следующие шаги:
        1. Открыть страницу https://suninjuly.github.io/math.html.
        2. Считать значение для переменной x.
        3. Посчитать математическую функцию от x (код для этого приведён ниже).
        4. Ввести ответ в текстовое поле.
        5. Отметить checkbox "I'm the robot".
        6. Выбрать radiobutton "Robots rule!".
        7. Нажать на кнопку Submit. ✍️---
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    # Шаги. Инициализация драйвера и открытие браузера
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    # Шаги. Поиск элемента с id="input_value"
    input_value_element = browser.find_element(By.ID, "input_value")
    x = float(input_value_element.text)  # Получение значения из элемента с id="input_value"

    # Шаги. Вычисление результата
    result = math.log(abs(12 * math.sin(x)))
    """
    math.sin(x) — вычисляет синус "x" (в радианах).
    12 * math.sin(x) — умножает результат на 12.
    abs(12 * math.sin(x)) — вычисляет абсолютное значение результата.
    math.log(abs(12 * math.sin(x))) — вычисляет натуральный логарифм от абсолютного значения.
    """

    # Шаги. Ввод ответа в текстовое поле
    answer_control_form = browser.find_element(By.ID, "answer")
    answer_control_form.send_keys(str(result))

    # Шаги. Отметка checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Шаги. Выбор radiobutton "Robots rule!"
    radio_robot = browser.find_element(By.ID, "robotsRule")
    radio_robot.click()

    # Шаги. Нажатие на кнопку Submit
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

    # Ожидание для визуальной оценки результата
    time.sleep(10)
    """
    # Пока не работает с автоформой Google Chrome
    
    # Ожидание появления модального окна
    alert = WebDriverWait(browser, 20).until(EC.alert_is_present())

    # Получение текста из модального окна
    alert_text = alert.text

    # Проверка текста на соответствие ожидаемому сообщению
    expected_message = "Congratulations, you've passed the task!"
    if expected_message in alert_text:
        print("Тест пройден успешно!")
    else:
        print("Тест не пройден. Ожидаемое сообщение не найдено.")

    # Нажатие на кнопку "OK" в модальном окне
    alert.accept()

    # Ожидание для визуальной оценки результата
    time.sleep(20)
"""

finally:
    browser.quit()




