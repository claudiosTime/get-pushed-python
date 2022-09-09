import pytest

from pushed_py.PushedPy import Config

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
CLIENT_ALIAS = "CLIENT_ALIAS"

def pushed_config():
    return Config(CLIENT_ID, CLIENT_SECRET, CLIENT_ALIAS)

def test_get_client_id(pushed_config):
    assert pushed_config.client_id == CLIENT_ID