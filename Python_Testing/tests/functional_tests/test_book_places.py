from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestApplication:
    """ Classe de tests fonctionnels de l'application """

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
        """ Test accès à la page de connexion """
        assert "Welcome to the GUDLFT Registration Portal!"\
            in self.driver.find_element(By.TAG_NAME, 'h1').text

    def _signin(self):
        """ Methode privée - Connecte un uitlisateur """
        email = self.driver.find_element(By.NAME, 'email')
        email.send_keys("john@simplylift.co")
        email.submit()

    def test_signin(self):
        """ Test la connexion d'un utilisateur """
        self._signin()
        assert 'Welcome, john@simplylift.co'\
            in self.driver.find_element(by=By.TAG_NAME, value='h2').text

    def test_points_display_access(self):
        """ Test l'accès au tableau des points """
        button = self.driver.find_element(By.XPATH, '/html/body/a/button')
        button.click()
        assert 'Table of points by club'\
            in self.driver.find_element(by=By.TAG_NAME, value='h1').text
        button = self.driver.find_element(By.XPATH, '/html/body/a/button')
        button.click()
        assert "Welcome to the GUDLFT Registration Portal!"\
            in self.driver.find_element(By.TAG_NAME, 'h1').text

    def test_book_places(self):
        """ Test la réservation de places pour une compétition """
        self._signin()
        book_places_button = self.driver.find_elements(
            By.LINK_TEXT, 'Book Places')[1]
        book_places_button.click()
        assert self.driver.current_url ==\
            'http://127.0.0.1:5000/book/Fall%20Classic/Simply%20Lift'
        form = self.driver.find_element(By.NAME, 'places')
        form.send_keys(2)
        book_button = self.driver.find_element(
            By.XPATH, '/html/body/form/button')
        book_button.click()
        assert self.driver.current_url ==\
            'http://127.0.0.1:5000/purchasePlaces'
        assert 'Great-booking complete!'\
            in self.driver.find_element(By.XPATH, '/html/body/ul[1]/li').text

    def test_logout(self):
        """ Test la déconnexion d'un utitilisateur """
        self._signin()
        logout_button = self.driver.find_element(By.LINK_TEXT, 'Logout')
        logout_button.click()
        assert self.driver.current_url == 'http://127.0.0.1:5000/'
