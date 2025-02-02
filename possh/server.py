import socket
import pickle as pkl
from .director import _apidict

class Server:
    def __init__(self, startImmediately: bool=True, port: int=56789):
        self._port = port
        if startImmediately:
            self.start()

    def start(self):
        # Begin a simple TCP server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', self._port))
            # Let's just loop after every connection to get the next one for now
            while True:
                print("Waiting for a connection...")
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    alldata = b''
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break

                        # Do simple concat for now
                        alldata += data

                    # Once complete, process the instructions
                    print(alldata)
                    plotInstructions = self._deserializePlotInstructions(alldata)
                    key, args, kwargs = plotInstructions
                    _apidict[key](*args, **kwargs)

    def _deserializePlotInstructions(self, pkldata: bytes):
        # Use pickle to get all args and kwargs
        return pkl.loads(pkldata)

_server = Server()

# ============= Developmental testing
if __name__ == '__main__':
    pass
