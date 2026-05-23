import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step('Create a new object')
    def create_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.url}/object',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
