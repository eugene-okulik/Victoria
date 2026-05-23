import pytest
import allure


TEST_DATA = [
    {"name": "DOOR1", "data": {"color": "", "size": ""}},
    {"name": "door 2", "data": {"color": "PINK", "size": "large"}},
    {"name": "door_301!", "data": {"color": "blue", "size": "SMALL"}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_object(create_object_endpoint, data, session_start_complete, before_after_each_test):
    create_object_endpoint.create_object(payload=data)
    create_object_endpoint.check_response_status_200()
    create_object_endpoint.check_object_contains_expected_values(
        expected_name=data['name'],
        expected_color=data['data']['color'],
        expected_size=data['data']['size']
    )


@allure.feature('Test Objects')
@allure.story('Getting Objects Info')
@allure.title('Get all existent objects')
@pytest.mark.critical
def test_get_objects(get_objects_endpoint, before_after_each_test):
    get_objects_endpoint.get_objects()
    get_objects_endpoint.check_response_status_200()
    get_objects_endpoint.check_objects_list_is_not_empty()


@allure.feature('Test Objects')
@allure.story('Getting Objects Info')
@allure.title('Get one specific object')
def test_get_object(get_object_endpoint, new_object_id, before_after_each_test):
    get_object_endpoint.get_object(object_id=new_object_id)
    get_object_endpoint.check_response_status_200()
    get_object_endpoint.check_object_id(expected_object_id=new_object_id)
    get_object_endpoint.check_json_structure()


@allure.feature('Test Objects')
@allure.story('Manipulating Objects')
@allure.title('Update object data')
def test_update_object(update_object_endpoint, new_object_id, before_after_each_test):
    body = {
        "name": "Door_1",
        "data": {"color": "black", "size": "small"}
    }
    update_object_endpoint.update_object(object_id=new_object_id, payload=body)
    update_object_endpoint.check_response_status_200()
    update_object_endpoint.check_object_contains_expected_values(
        expected_name=body['name'],
        expected_color=body['data']['color'],
        expected_size=body['data']['size']
    )


@allure.feature('Test Objects')
@allure.story('Manipulating Objects')
@allure.title('Update object data partially')
@pytest.mark.medium
def test_update_object_partially(update_object_partially_endpoint, new_object_id, before_after_each_test):
    body = {
        "name": "Door_2",
        "data": {"color": "green"}
    }
    update_object_partially_endpoint.update_object_partially(object_id=new_object_id, payload=body)
    update_object_partially_endpoint.check_response_status_200()
    update_object_partially_endpoint.check_object_contains_expected_values(
        expected_name=body['name'],
        expected_color=body['data']['color'],
        expected_size="medium"
    )


@allure.feature('Test Objects')
@allure.story('Manipulating Objects')
@allure.title('Delete object')
def test_delete_object(delete_object_endpoint, get_object_endpoint, new_object_id, before_after_each_test):
    delete_object_endpoint.delete_object(object_id=new_object_id)
    delete_object_endpoint.check_response_status_200()
    get_object_endpoint.get_object(object_id=new_object_id)
    get_object_endpoint.check_response_status_404()
