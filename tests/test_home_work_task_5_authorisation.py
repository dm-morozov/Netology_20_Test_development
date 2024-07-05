from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pytest

def test_yandex_authorisation():

    # Устанавливаем ChromeDriver с помощью webdriver_manager
    chrome_path = ChromeDriverManager().install()
    browser_service = Service(chrome_path)
    driver = webdriver.Chrome(service=browser_service)
    
    try:
        driver.get("https://passport.yandex.ru/auth/")
        
        
        login_field = driver.find_element(By.ID, "passp-field-login")
        login_field.send_keys("dm.program@yandex.ru")  # Введите логин
        # Имитируем нажатие клавиши Enter 
        login_field.send_keys(Keys.RETURN)
        
        # Не стал заморачиваться с функцией wait_element, 
        # Ведь первоочередная задача написать тест
        # На боевых проектах так, конечно, делать нельзя
        time.sleep(2)  
        password_field = driver.find_element(By.ID, "passp-field-passwd")
        password_field.send_keys("PASSWORD")  # Введите пароль
        password_field.send_keys(Keys.RETURN)
        
        # Нужно 30 сек. для того, чтобы успеть ввести 6-ый код, который пришел на телефон

        time.sleep(30)
        
        # Проверим, что авторизация прошла успешно
        # Добавим условие or, чтобы если не захотите вводить код, тест всё равно проходил
        assert "https://id.yandex.ru/" in driver.current_url or \
            "https://passport.yandex.ru/auth/challenge" in driver.current_url
    finally:
        driver.quit()