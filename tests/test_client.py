import pytest

from pushed_py.PushedPy import send
from pushed_py.PushedPyException import NotificationSendFailed

def test_send_exception(config):
    with pytest.raises(NotificationSendFailed) as e:
        send("Test invio messaggio", config)