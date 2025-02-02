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
            # Let's just loop after every connection to get the next one for now
            while True:
                print("Waiting for a connection...")
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(data)

# ============= Developmental testing
if __name__ == '__main__':
    server = Server()
