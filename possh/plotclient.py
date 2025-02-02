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

def axis(*args, **kwargs):
    _client.connectAndSend(
        _client.serializePlotInstructions(
            'pyplot.axis', *args, **kwargs
        )
    )

# ========== Dev testing
if __name__ == '__main__':
    import numpy as np
    figure()
    plot((1,2,3), (4,5,1))

    figure()
    plot(np.arange(100)*0.01, np.sin(np.arange(100)*0.01), 'rx-')
    axis([0, 2, -1, 1])
    show()

