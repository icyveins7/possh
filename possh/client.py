import socket
import os
from typing import Optional
import pickle as pkl

class Client:
    def __init__(self, serverIp: Optional[str] = None, serverPort: int = 56789):
        """
        Instantiates the client for the possh server.

        Default arguments will assume the possh server is being hosted by the
        current SSH client that is connected.

        SSH Client   ------------> SSH Server
        possh server <------------ possh client

        Parameters
        ----------
        serverIp : str | None
            The IP address of the possh server. Defaults to None,
            which will assume you are connected over SSH and attempt to
            parse your client IP address.

        serverPort : int
            The port number of the possh server. Defaults to 56789.
        """
        if serverIp is None:
            self._serverIp, _, _ = self.getSshSource()
        else:
            self._serverIp = serverIp
        self._serverPort = serverPort

    def getSshSource(self) -> tuple[str, int, int]:
        """
        Retrieve and return the components populated in the environment
        variable SSH_CLIENT.

        You probably don't need to call this directly.

        Returns
        -------
        client_ip : str
            The IP address of the SSH client

        client_port : int
            The port number of the SSH client

        server_port : int
            The port number of the SSH server
        """
        ssh_client = os.getenv('SSH_CLIENT')
        if ssh_client is None:
            raise ValueError('SSH_CLIENT environment variable not set')

        client_ip, client_port, server_port = ssh_client.split()
        return (client_ip, int(client_port), int(server_port))

    def connectAndSend(self, data: bytes):
        """
        Connect to the Server instance, send the data and disconnect.
        This is probably the most used method.

        Parameters
        ----------
        data : bytes
            The data to send.
        """
        # Start a simple client connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self._serverIp, self._serverPort))
            s.sendall(data)

    def serializePlotInstructions(self, key: str, *args, **kwargs) -> bytes:
        """
        Serializes a generic set of plot instructions using pickle.

        This should be deserialized by the server based on the key supplied.

        Parameters
        ----------
        key : str
            Key for the server to handle the plot instruction.

        *args
            Arguments supplied with the plot instruction.

        **kwargs
            Keyword arguments supplied with the plot instruction.

        Returns
        -------
        data : bytes
            Pickled data to be sent.
        """
        data = pkl.dumps((key, args, kwargs))
        print(data)
        return data

# TODO: is there a better way other than to just instantiate here? feels unsafe..
_client = Client()


# ============= Some developmental testing
if __name__ == '__main__':
    print(_client.getSshSource())
    _client.connectAndSend(b'Test data')

