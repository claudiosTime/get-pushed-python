from requests import post

from pushed_py.PushedPyException import NotificationSendFailed

PUSHED_SERVICE_URL = "https://api.pushed.co/1"

class Config:
    
    def __init__(self, client_id, client_secret, client_alias = None):
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

def send(message: str, config: Config, target: str = "app") -> bool:
    payload = {
        "app_key": Config.client_id,
        "app_secret": Config.client_secret,
        "target_type": target,
        "content": message
    }

    r = requests.post(f"{PUSHED_SERVICE_URL}/push", data=payload)
    
    if not r.ok:
        NotificationSendFailed()
    else:
        return True