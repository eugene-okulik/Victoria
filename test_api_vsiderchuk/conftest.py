import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.update_object_partially import UpdateObjectPartially
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.get_objects import GetObjects


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
def new_object_id(create_object_endpoint, delete_object_endpoint):
    body = {
        "name": "Door",
        "data": {"color": "white", "size": "medium"}
    }
    create_object_endpoint.create_object(payload=body)
    yield create_object_endpoint.object_id
    delete_object_endpoint.delete_object(object_id=create_object_endpoint.object_id)


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def update_object_partially_endpoint():
    return UpdateObjectPartially()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def get_objects_endpoint():
    return GetObjects()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
