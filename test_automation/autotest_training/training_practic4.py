from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим обязательные поля и вводим произвольные значения
    first_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class input')  # First Name

    last_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class input')  # Last Name

    email_input = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class input')  # Email

    first_name_input.send_keys('Danil')
    last_name_input.send_keys('Shevchenko')
    email_input.send_keys('shdan@textmail.com')

    # Отсылаем заполненную форму
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()

    # Ждём перезагрузки страницы
    time.sleep(1)

    # Получаем заголовок h1 и сравниваем с нужным текстом
    success_message = browser.find_element(By.TAG_NAME, 'h1').text
    assert "Congratulations! You have successfully registered!" == success_message, f'Ошибка регистрации: "{success_message}"'

finally:
    # Время на визуальное подтверждение результатов
    time.sleep(10)
    # Закрытие браузера
    browser.quit()

    '''
        Если результат проверки "Поздравляем! Вы успешно зарегистрировались!" == текст_приветствия
    вернет значение (False), далее выполнится код "Assert False". 
    Он бросает выводы "AssertionError" и номер строки, в которой произошла ошибка. 
        Если код написан правильно и работал раньше, такой результат равносилен тому, что наш 
    автотест обнаружил баг в тестируемом веб-приложении. 
        Если результат проверки вернет True, то выполнится выражение утверждать, что это правда. 
    В этом коде тест завершается без ошибок — проходит успешно.
    '''