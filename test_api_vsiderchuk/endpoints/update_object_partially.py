import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObjectPartially(Endpoint):
    @allure.step('Update object partially')
    def update_object_partially(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/object/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
