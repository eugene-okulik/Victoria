import requests


def get_all_objects():
    response = requests.get("http://objapi.course.qa-practice.com/object")
    assert response.status_code == 200, 'Status code is incorrect'


def new_object():
    body = {
        "name": "Door",
        "data": {
            "color": "white",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    return response.json()['id']


def get_object(object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}')
    return response


def put_object(object_id):
    body = {
        "name": "Door_1",
        "data": {
            "color": "black",
            "size": "small"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{object_id}', json=body, headers=headers)
    return response


def patch_object(object_id):
    body = {
        "name": "Door_2",
        "data": {
            "color": "green"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{object_id}', json=body, headers=headers)
    return response


def delete_object(object_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    return response


object_id = new_object()


put_response = put_object(object_id)
test_object = get_object(object_id).json()
assert put_response.status_code == 200, 'Status code is incorrect'
assert test_object['name'] == 'Door_1', 'Name is incorrect'
assert test_object['data']['color'] == 'black', 'Color is incorrect'
assert test_object['data']['size'] == 'small', 'Size is incorrect'

patch_response = patch_object(object_id)
test_object = get_object(object_id).json()
assert patch_response.status_code == 200, 'Status code is incorrect'
assert test_object['name'] == 'Door_2'
assert test_object['data']['color'] == 'green', 'Color is incorrect'
assert test_object['data']['size'] == 'small', 'Size is incorrect'

delete_response = delete_object(object_id)
assert delete_response.status_code == 200, 'Status code is incorrect'
check_deletion = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}')
assert check_deletion.status_code == 404, 'Status code is incorrect'
