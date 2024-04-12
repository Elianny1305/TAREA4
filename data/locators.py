from selenium.webdriver.common.by import By

class LinkedInLocators:
    # Botones para el inicio de sesión
    USERNAME_INPUT = (By.NAME, 'session_key')
    PASSWORD_INPUT = (By.NAME, 'session_password')
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Botones para publicar un mensaje
    POST_BUTTON = (By.XPATH, '//button[contains(@class, "artdeco-button--muted") and contains(@class, "artdeco-button--tertiary") and contains(@class, "share-box-feed-entry__trigger")]')
    POST_INPUT = (By.CLASS_NAME, "ql-editor")
    PUBLISH_BUTTON = (By.XPATH, '//button[contains(text(), "Publicar")]')

    # Elementos para verificar si el mensaje se publicó correctamente
    MESSAGE_CONTAINER = (By.XPATH, '//div[contains(@class, "feed-shared-update-v2")]/div[contains(@class, "feed-shared-update-v2__content")]/span')
