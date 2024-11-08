from locust import HttpUser, task
import time

class NewsletterUser(HttpUser):
    @task
    def login_to_newsletter(self):
        self.client.get("/welcome")
        time.sleep(5)
        with self.client.get("/welcome?identifier=AQ", catch_response=True) as response:
            if "AQ".lower() not in response.text.lower():
                response.failure("User AQ not logged in")


