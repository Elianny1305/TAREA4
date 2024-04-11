import unittest
import time
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
        self.driver.maximize_window()  # Maximizar la ventana del navegador para evitar problemas de visibilidad

    def tearDown(self):
        self.driver.quit()

    def test_login_and_post(self):
        # Iniciar sesión en LinkedIn
        self.login_to_linkedin()

        # Publicar un mensaje
        message = "Holaaaaa, cómo están"
        self.post_message(message)

        # Comprobar si se publicó correctamente
        if self.is_message_published(message):
            print("Message posted successfully.")
        else:
            print("Failed to post message.")

    def login_to_linkedin(self):
        self.driver.get('https://www.linkedin.com/login')

        # Leer el usuario y la contraseña desde los archivos de texto
        with open(r"C:\Users\Elianny\Downloads\username.txt") as myUser:
            username = myUser.read().strip()  # Eliminar espacios en blanco adicionales

        with open(r"C:\Users\Elianny\Downloads\password.txt") as myPass:
            password = myPass.read().strip()  # Eliminar espacios en blanco adicionales

        # Introducir el usuario y la contraseña en los campos correspondientes
        email = self.driver.find_element(By.NAME, 'session_key')
        password_field = self.driver.find_element(By.NAME, 'session_password')

        email.send_keys(username)
        password_field.send_keys(password)

        # Hacer clic en el botón de inicio de sesión
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Esperar hasta que se cargue la página de inicio después del inicio de sesión
        WebDriverWait(self.driver, 10).until(EC.url_contains("https://www.linkedin.com/feed/"))

    def post_message(self, message):
        # Esperar a que el botón de publicación esté visible
        box_post = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class, "artdeco-button--muted") and contains(@class, "artdeco-button--tertiary") and contains(@class, "share-box-feed-entry__trigger")]')))

        # Hacer clic en el botón de publicación
        box_post.click()

        # Encontrar el campo de entrada de la publicación y escribir un mensaje
        post_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "ql-editor")))
        post_input.send_keys(message)

        # Hacer clic en el botón de publicar
        post_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Publicar")]')))
        post_button.click()

    def is_message_published(self, message):
        # Esperar hasta que aparezca el mensaje publicado
        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, f'//div[contains(@class, "feed-shared-update-v2")]/div[contains(@class, "feed-shared-update-v2__content")]/span[contains(text(), "{message}")]'), message))
            return True
        except:
            return False

if __name__ == "__main__":
    unittest.main()
