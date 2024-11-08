from locust import HttpUser, task
import time

class NewsletterUser(HttpUser):
    @task
    def login_to_newsletter(self):
        self.client.get("/welcome")
        time.sleep(5)
        with open('./ids.csv', 'r') as id_file:
            for line in id_file.readlines():
                identifier = line.strip()
                with self.client.get(f"/welcome?identifier={identifier}", catch_response=True) as response:
                    if identifier.lower() not in response.text.lower():
                        response.failure(f"User {identifier} not logged in")


