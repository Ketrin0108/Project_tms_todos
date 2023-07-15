import pytest
from todos.tests.test_app import test_data

from todos.models import ToDo


@pytest.mark.django_db
def test_get_todos(client, test_data):
    response = client.get("/api/todo/")
    assert response.status_code == 200
    assert len(response.json()["todos"])== 3
    assert response.json()["todos"][0]["name"] == "go to the store"


# проверка на получение todo
@pytest.mark.django_db
def test_get_todo(client, test_data):
    response = client.get("/api/todo/1/")
    assert response.status_code == 200
    assert response.json() == {
        'todo': {
            'completed': False,
            'description': 'out of products',
            'id': 1,
            'name': 'go to the store',
            'user': 2
        }
    }

#проверка на создание todo
@pytest.mark.django_db
def test_create_todo(client, test_data):
    response = client.post("/api/todo/", data={
        "name": "new todo",
        "description": "new todo",
        "user": 2,

    })
    assert response.status_code == 200
    assert response.json() == {
        'id': 4,
        'name': 'new todo',
        'description': 'new todo',
        'user': 2,
        'completed': False
    }

# проверка на удадение todo
@pytest.mark.django_db
def test_delete_todo(client, test_data):
    response = client.delete("/api/todo/1/")
    assert response.status_code == 200
    assert response.json() == {'message': 'ToDo successfully deleted', 'status': 204}
    with pytest.raises(ToDo.DoesNotExist):
        ToDo.objects.get(id=1)

# проверка на ошибки 400
@pytest.mark.django_db
def test_create_todo_returns_form_errors(client, test_data):
    response = client.post("/api/todo/", data={
        'description': 'new todo',
        'user': 2,
        'completed': False

    })
    assert response.status_code == 400
    assert response.json() == {
        'errors': {'name': ['This field is required.']}
    }
