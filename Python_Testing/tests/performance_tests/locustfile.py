from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get('/')

    @task
    def points_display(self):
        self.client.get('/points_display')
    
    @task
    def login(self):
        self.client.post('/showSummary', {'email':'john@simplylift.co'})

    @task
    def purchase_places(self):
        data = {
            'club': "Simply Lift",
            'competition': "Fall Classic",
            'places': 1
        }
        self.client.post("/purchasePlaces", data)