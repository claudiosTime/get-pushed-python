import pytest

from pushed_py.PushedPy import Config

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
CLIENT_ALIAS = "CLIENT_ALIAS"

@pytest.fixture
def config():
    return Config(CLIENT_ID, CLIENT_SECRET, CLIENT_ALIAS)

def test_get_client_id(config):
    assert config.client_id == CLIENT_ID

def test_get_client_secret(config):
    assert config.client_secret == CLIENT_SECRET

def test_get_client_alias(config):
    assert config.client_alias == CLIENT_ALIAS