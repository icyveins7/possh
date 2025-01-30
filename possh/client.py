import socket
import os

class Client:
    def __init__(self, port: int=56789):
        self._port = port

    def getSshSource(self):
        # We query the SSH_CLIENT environment variable and parse it
        ssh_client = os.getenv('SSH_CLIENT')
        return ssh_client

    def connect(self):
        pass


# ============= Some developmental testing
if __name__ == '__main__':
    client = Client()
    print(client.getSshSource())

