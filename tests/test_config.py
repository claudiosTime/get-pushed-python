import pytest

from .conftest import CLIENT_ALIAS, CLIENT_SECRET, CLIENT_ID

def test_get_client_id(config):
    assert config.client_id == CLIENT_ID

def test_get_client_secret(config):
    assert config.client_secret == CLIENT_SECRET

def test_get_client_alias(config):
    assert config.client_alias == CLIENT_ALIAS