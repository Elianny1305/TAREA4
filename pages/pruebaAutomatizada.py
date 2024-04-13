import unittest
import time
import os
import pytest
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class LinkedInTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(executable_path=r'chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.test
    def test_login_and_post(self):  # Marcar la función como una prueba con pytest
        start_time = time.time()  # Capturando el tiempo de inicio
        self.take_screenshot("00_before_login")
        
        self.login_to_linkedin()
        
        self.take_screenshot("logged_in")

        message = "Holaaaaa, cómo están"
        self.post_message(message)
        self.take_screenshot("posted_message")

        self.view_post()
        self.take_screenshot("viewed_post")

        self.react_to_post()
        self.take_screenshot("reacted_to_post")

        end_time = time.time()  # Capturando el tiempo de finalización
        execution_time = end_time - start_time  # Calculando el tiempo de ejecución
        print(f"Execution Time: {execution_time} seconds")

    def login_to_linkedin(self):
        self.driver.get('https://www.linkedin.com/login')
        
        # Esperar a que los elementos de la página de inicio de sesión estén presentes
        email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'session_key')))
        password_field = self.driver.find_element(By.NAME, 'session_password')
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        # Tomar captura de pantalla antes de ingresar las credenciales
        self.take_screenshot("before_login_details")
        
        with open(r"C:\Users\Elianny\Downloads\username.txt") as myUser:
            username = myUser.read().strip()
        with open(r"C:\Users\Elianny\Downloads\password.txt") as myPass:
            password = myPass.read().strip()

        email.send_keys(username)
        password_field.send_keys(password)

        submit_button.click()
        
        WebDriverWait(self.driver, 10).until(EC.url_contains("https://www.linkedin.com/feed/"))

        # Tomar captura de pantalla después de iniciar sesión
        self.take_screenshot("after_login_details")

    def post_message(self, message):
        box_post = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class, "artdeco-button--muted") and contains(@class, "artdeco-button--tertiary") and contains(@class, "share-box-feed-entry__trigger")]')))
        box_post.click()

        post_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "ql-editor")))
        post_input.send_keys(message)
        post_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def view_post(self):
        view_post_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="artdeco-toast-item__cta"]')))
        view_post_button.click()

    def react_to_post(self):
        react_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@aria-hidden="true" and contains(@class, "artdeco-button__text") and contains(@class, "react-button__text") and contains(@class, "social-action-button__text") and contains(@class, "react-button__text--like")]')))
        react_button.click()

    def take_screenshot(self, name):
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join('screenshots', f'{name}_{timestamp}.png')

        self.driver.save_screenshot(screenshot_path)

if __name__ == "__main__":
    unittest.main()
    
    # Llamada a pytest con argumentos para generar el reporte HTML después de que se ejecuten todas las pruebas
    pytest.main(["-v", "--html=report.html"])
