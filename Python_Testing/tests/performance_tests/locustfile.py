from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    """ Classe de test de performance Locust """
    @task
    def home(self):
        """ Tâche accès à home """
        self.client.get('/')

    @task
    def points_display(self):
        """ Tâche accès à points_display """
        self.client.get('/points_display')

    @task
    def login(self):
        """ Tâche accès à showSummary """
        self.client.post('/showSummary', {'email': 'john@simplylift.co'})

    @task
    def purchase_places(self):
        """ Tâche accès à purchasePlaces """
        data = {
            'club': "Simply Lift",
            'competition': "Fall Classic",
            'places': 1
        }
        self.client.post("/purchasePlaces", data)
