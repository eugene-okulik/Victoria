from locust import task, HttpUser, between
import random


class ObjectUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def create_object(self):
        payload = {"name": "door 2", "data": {"color": "PINK", "size": "large"}}
        headers = {'Content-Type': 'application/json'}
        self.client.post(
            '/object',
            json=payload,
            headers=headers
        )

    @task(1)
    def update_object(self):
        payload = {"name": "door_UPD", "data": {"color": "PINK", "size": "large"}}
        headers = {'Content-Type': 'application/json'}
        self.client.put(
            f'/object/{random.choice([312, 320, 451, 454])}',
            json=payload,
            headers=headers
        )

    @task(3)
    def get_object(self):
        self.client.get(f'/object/{random.choice([312, 320, 451, 454])}')

    @task(6)
    def get_objects(self):
        self.client.get('/object')
