"""
Базовый класс для всех Page Objects.
Содержит общие методы для работы с элементами DOM.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

from config.config import EXPLICIT_WAIT_TIMEOUT


class BasePage:
    """
    Базовый класс для всех page objects.
    Предоставляет общие методы для взаимодействия с браузером и элементами.
    """
    
    def __init__(self, driver: WebDriver):
        """
        Инициализирует BasePage.
        
        :param driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT_TIMEOUT)
    
    def find_element(self, locator: tuple):
        """
        Находит элемент и ждёт, пока он будет видимым.
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator: tuple):
        """
        Находит список элементов и ждёт, пока они будут присутствовать в DOM.
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        :return: список WebElements
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator: tuple):
        """
        Кликает по элементу после ожидания его видимости.
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator: tuple, text: str):
        """
        Вводит текст в элемент.
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        :param text: текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator: tuple) -> str:
        """
        Получает текст элемента.
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        :return: текст элемента
        """
        element = self.find_element(locator)
        return element.text
    
    def wait_for_element(self, locator: tuple):
        """
        Ждёт, пока элемент будет присутствовать в DOM.
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        :return: WebElement
        """
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def hover(self, locator: tuple):
        """
        Наводит курсор на элемент (hover).
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        """
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
    
    def scroll_to_element(self, locator: tuple):
        """
        Скроллит страницу к элементу.
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def scroll_to_bottom(self):
        """
        Скроллит страницу в самый низ.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def switch_to_new_tab(self):
        """
        Переключается на новую вкладку (предполагается, что она только что открылась).
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])
    
    def get_current_url(self) -> str:
        """
        Получает текущий URL страницы.
        
        :return: текущий URL
        """
        return self.driver.current_url
    
    def is_element_visible(self, locator: tuple) -> bool:
        """
        Проверяет, видим ли элемент на странице.
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        :return: True если видимый, False если нет
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def is_element_present(self, locator: tuple) -> bool:
        """
        Проверяет, присутствует ли элемент в DOM.
        
        :param locator: кортеж (By.XPATH/CSS_SELECTOR, "локатор")
        :return: True если присутствует, False если нет
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
