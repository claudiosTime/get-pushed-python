from requests import post

PUSHED_SERVICE_URL = "https://api.pushed.co/1"

class Config:
    
    def __init__(self, client_id, client_secret, client_alias):
        self._client_id = client_id
        self._client_secret = client_secret
        self._client_alias = client_alias

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        self._client_id = client_id

    @property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        self._client_secret = client_secret

    @property
    def client_alias(self):
        return self._client_alias

    @client_alias.setter
    def client_alias(self, client_alias):
        self._client_alias = client_alias
