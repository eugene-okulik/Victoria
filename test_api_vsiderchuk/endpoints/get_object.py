import requests
import allure
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step('Get Single Objects')
    def get_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/object/{object_id}',
            headers=headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
        else:
            self.json = None

        return self.response
