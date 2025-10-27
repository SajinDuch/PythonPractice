"""
https://stepik.org/course/575/syllabus

---✍️ ЗАДАНИЕ: Stepik
0. На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:
    1. Добавьте в самый верх своего кода import math
    2. Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
    3. Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти,
     зашифрован формулой: str(math.ceil(math.pow(math.pi, math.e)*10000)) (можно вставить данное выражение в свой код,
      а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде)
    4. Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
    5. Заполните скриптом форму так же как вы делали в предыдущем шаге урока
    6. После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание ✍️---
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Рассчитываем значение ссылки
search_link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser = webdriver.Chrome()    # Создаем экземпляр браузера

browser.get('http://suninjuly.github.io/find_link_text')    # Открываем главную страницу

# Находим нужную ссылку по тексту
link = browser.find_element(By.LINK_TEXT, search_link_text)

link.click()    # Клик по ссылке

time.sleep(1)     # Пауза, чтобы убедиться, что страница открылась

# Заполняем форму
input1 = browser.find_element(By.NAME, 'first_name')
input1.send_keys('Danil')

input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys('Shevchenko')

input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
input3.send_keys('Rostov-on0Don')

input4 = browser.find_element(By.ID, 'country')
input4.send_keys('Russia')

button = browser.find_element(By.CSS_SELECTOR, 'button.btn')    # Отсылаем заполненную форму
button.click()

time.sleep(30)      # Оставляем окно открытым на 30 сек., чтобы посмотреть результат

browser.quit()       # Закрываем браузер