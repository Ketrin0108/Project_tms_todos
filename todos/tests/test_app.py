import pytest
from django.test import Client

from todos.fill_db import create_initial_db


@pytest.fixture
def client():
    return Client()

@pytest.fixture
def test_data():
    create_initial_db()
