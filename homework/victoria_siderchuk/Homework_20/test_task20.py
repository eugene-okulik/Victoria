import requests
import pytest
import allure

BASE_URL = "http://objapi.course.qa-practice.com"
OBJECT_ENDPOINT = f"{BASE_URL}/object"


@pytest.fixture(scope='session')
def session_start_complete():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(scope='function')
def before_after_each_test():
    print("\nBefore test")
    yield
    print("\nAfter test")


@pytest.fixture()
def new_object_id():
    body = {
        "name": "Door",
        "data": {"color": "white", "size": "medium"}
    }
    response = requests.post(OBJECT_ENDPOINT, json=body)
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'{OBJECT_ENDPOINT}/{object_id}')


@pytest.fixture()
def object_to_be_deleted():
    body = {
        "name": "Door To Delete",
        "data": {}
    }
    response = requests.post(OBJECT_ENDPOINT, json=body)
    return response.json()['id']


@allure.feature('Test Objects')
@allure.story('Manipulating Objects')
@allure.title('Create object')
@pytest.mark.parametrize('name, color, size', [
    ('DOOR1', '', ''),
    ('door 2', 'PINK', 'large'),
    ('door_301!', 'blue', 'SMALL')
])
def test_create_object(session_start_complete, before_after_each_test, name, color, size):
    with allure.step('Prepare test data'):
        body = {
            "name": name,
            "data": {"color": color, "size": size}
        }
    with allure.step('Run request to create object'):
        create_response = requests.post(OBJECT_ENDPOINT, json=body)
    with allure.step('Check response status code'):
        assert create_response.status_code == 200
    with allure.step('Check response body'):
        created_object = create_response.json()
        assert created_object['name'] == name
        assert created_object['data']['color'] == color
        assert created_object['data']['size'] == size
        created_object_id = created_object['id']
    with allure.step('Delete the created object'):
        requests.delete(f'{OBJECT_ENDPOINT}/{created_object_id}')


@allure.feature('Test Objects')
@allure.story('Getting Objects Info')
@allure.title('Get all existent objects')
@pytest.mark.critical
def test_get_all_objects(before_after_each_test):
    response = requests.get(OBJECT_ENDPOINT)
    assert response.status_code == 200


@allure.feature('Test Objects')
@allure.story('Getting Objects Info')
@allure.title('Get one specific object')
def test_get_single_object(new_object_id, before_after_each_test):
    response = requests.get(f'{OBJECT_ENDPOINT}/{new_object_id}')
    assert response.status_code == 200
    test_object = response.json()
    assert test_object['id'] == new_object_id
    assert 'name' in test_object
    assert 'data' in test_object


@allure.feature('Test Objects')
@allure.story('Manipulating Objects')
@allure.title('Update object data')
def test_put_object(new_object_id, before_after_each_test):
    body = {
        "name": "Door_1",
        "data": {"color": "black", "size": "small"}
    }
    put_response = requests.put(f'{OBJECT_ENDPOINT}/{new_object_id}', json=body)
    assert put_response.status_code == 200
    test_object = requests.get(f'{OBJECT_ENDPOINT}/{new_object_id}').json()
    assert test_object['name'] == 'Door_1'
    assert test_object['data']['color'] == 'black'
    assert test_object['data']['size'] == 'small'


@allure.feature('Test Objects')
@allure.story('Manipulating Objects')
@allure.title('Update object data partially')
@pytest.mark.medium
def test_patch_object(new_object_id, before_after_each_test):
    with allure.step('Prepare test data'):
        body = {
            "name": "Door_2",
            "data": {"color": "green"}
        }
    with allure.step('Run request to update object partially'):
        patch_response = requests.patch(f'{OBJECT_ENDPOINT}/{new_object_id}', json=body)
    with allure.step('Check response status code'):
        assert patch_response.status_code == 200
    test_object = requests.get(f'{OBJECT_ENDPOINT}/{new_object_id}').json()
    print(test_object)
    with allure.step('Check response body. Size should keep the old value.'):
        assert test_object['name'] == 'Door_2'
        assert test_object['data']['color'] == 'green'
        assert test_object['data']['size'] == 'medium'


@allure.feature('Test Objects')
@allure.story('Manipulating Objects')
@allure.title('Delete object')
def test_delete_object(object_to_be_deleted, before_after_each_test):
    delete_response = requests.delete(f'{OBJECT_ENDPOINT}/{object_to_be_deleted}')
    assert delete_response.status_code == 200
    get_check_deletion = requests.get(f'{OBJECT_ENDPOINT}/{object_to_be_deleted}')
    assert get_check_deletion.status_code == 404
