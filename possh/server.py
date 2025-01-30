import socket

class Server:
    def __init__(self, startImmediately: bool=True, port: int=56789):
        self._port = port
        if startImmediately:
            self.start()

    def start(self):
        # Begin a simple TCP server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', self._port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

