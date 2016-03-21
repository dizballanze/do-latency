import time

from .pyping import ping


def do_ping(host, count=10, timeout=10, udp=False, hook=None):
    results = []
    for i in range(0, count):
        results.append(ping(host, timeout, udp=udp))
        if hook is not None:
            hook()
    return "{:.3f}".format(sum(results) / count)
