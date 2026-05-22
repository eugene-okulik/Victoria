import requests
import allure
from endpoints.endpoint import Endpoint


class GetObjects(Endpoint):
    @allure.step('Get All Objects')
    def get_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/object',
            headers = headers
        )
        self.json = self.response.json()
        return self.response


    @allure.step('Check that objects list is not empty')
    def check_objects_list_is_not_empty(self):
        assert len(self.json) > 0
