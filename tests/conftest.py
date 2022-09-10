"""
conftest.py
"""

import pytest

from pushed_py.PushedPy import Config

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
CLIENT_ALIAS = "CLIENT_ALIAS"

@pytest.fixture
def config():
    return Config(CLIENT_ID, CLIENT_SECRET, CLIENT_ALIAS)