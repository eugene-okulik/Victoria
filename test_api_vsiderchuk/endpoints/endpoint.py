import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check response status is 200')
    def check_response_status_200(self):
        assert self.response.status_code == 200


    @allure.step('Check response status is 404')
    def check_response_status_404(self):
        assert self.response.status_code == 404


    @allure.step('Check that returned ID is the same as requested ID')
    def check_object_id(self, expected_object_id):
        assert self.json['id'] == expected_object_id


    @allure.step('Check JSON structure')
    def check_json_structure(self):
        assert 'name' in self.json
        assert 'data' in self.json


    @allure.step('Check that object contains expected values')
    def check_object_contains_expected_values(self, expected_name, expected_color, expected_size):
        assert self.json['name'] == expected_name
        assert self.json['data']['color'] == expected_color
        assert self.json['data']['size'] == expected_size
