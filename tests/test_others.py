
import os
import sys

import pytest
import argparse
from server import check_file
from server import app
from server import main


def test_create_file():
    assert (check_file("test.txt") == 0)
    return 0

def test_file_already_exists():
    assert (check_file("test.txt") == 1)
    os.remove("test.txt")
    return 0

def test_homepage():
    with app.test_client() as test_client:
        response = test_client.get('/')
    assert response.status_code == 200
    assert b"Servicio Web para Cadenas" in response.data
    return 0

