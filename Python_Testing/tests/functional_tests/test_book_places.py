import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


""" @pytest.fixture(scope="class")
def setUp(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.get('http://127.0.0.1:5000')
    driver.maximize_window()
    yield
    driver.quit()


@pytest.mark.usefixtures('setUp') """
class TestLambda:
    def setup_method(self, method):
        """ Initialisation du driver Google Chrome pour Selenium
        appelée au début de chaque test de la classe """
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            'excludeSwitches', ['enable-logging']
            )
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
            )
        self.driver.get('http://127.0.0.1:5000')
        self.driver.maximize_window()

    def teardown_method(self, method):
        """ Fermeture du driver Google Chrome pour Selenium
        appelée à la fin de chaque test de la classe """
        self.driver.quit()

    def test_registration_portal_access(self):
        assert "Welcome to the GUDLFT Registration Portal!"\
            in self.driver.find_element(By.TAG_NAME, 'h1').text

    def _signin(self):
        email = self.driver.find_element(By.NAME, 'email')
        email.send_keys("john@simplylift.co")
        email.submit()
    
    def test_signin(self):
        self._signin()
        assert 'Welcome, john@simplylift.co'\
            in self.driver.find_element(by=By.TAG_NAME, value='h2').text   
    
    def test_points_display_access(self):
        button = self.driver.find_element(By.XPATH,'/html/body/a/button')
        button.click()
        assert 'Table of points by club'\
            in self.driver.find_element(by=By.TAG_NAME, value='h1').text
        button = self.driver.find_element(By.XPATH,'/html/body/a/button')
        button.click()
        assert "Welcome to the GUDLFT Registration Portal!"\
            in self.driver.find_element(By.TAG_NAME, 'h1').text

    def test_book_places(self):
        self._signin()
        book_places_button = self.driver.find_elements(
            By.LINK_TEXT,'Book Places')[1]
        book_places_button.click()
        assert self.driver.current_url ==\
            'http://127.0.0.1:5000/book/Fall%20Classic/Simply%20Lift'
        form = self.driver.find_element(By.NAME,'places')
        form.send_keys(2)
        book_button = self.driver.find_element(
            By.XPATH, '/html/body/form/button')
        book_button.click()
        assert self.driver.current_url ==\
            'http://127.0.0.1:5000/purchasePlaces'
        assert 'Great-booking complete!'\
            in self.driver.find_element(By.XPATH, '/html/body/ul[1]/li').text
        
    def test_logout(self):
        self._signin()
        logout_button = self.driver.find_element(By.LINK_TEXT, 'Logout')
        logout_button.click()
        assert self.driver.current_url == 'http://127.0.0.1:5000/'
