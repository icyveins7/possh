from .client import _client
from typing import Optional

def figure(*args, **kwargs):
    _client.connectAndSend(
        _client.serializePlotInstructions(
            'pyplot.figure', *args, **kwargs
        )
    )

def plot(*args, **kwargs):
    _client.connectAndSend(
        _client.serializePlotInstructions(
            'pyplot.plot', *args, **kwargs
        )
    )

def show(*args, **kwargs):
    _client.connectAndSend(
        _client.serializePlotInstructions(
            'pyplot.show', *args, **kwargs
        )
    )

# ========== Dev testing
if __name__ == '__main__':
    figure()
    plot((1,2,3), (4,5,1))
    show()

