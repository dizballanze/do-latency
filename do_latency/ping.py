import time

from pyping import Ping, MAX_SLEEP


class ProgressPing(Ping):

    def __init__(self, *args, **kwargs):
        self.hook = kwargs.pop("hook", None)
        super(ProgressPing, self).__init__(*args, **kwargs)

    def receive_one_ping(self, current_socket):
        result = super(ProgressPing, self).receive_one_ping(current_socket)
        if self.hook is not None:
            self.hook()
        return result


def do_ping(host, count=10, timeout=1000, packet_size=55, udp=False, hook=None):
    ping = ProgressPing(host, timeout, packet_size, udp=udp, hook=hook)
    return ping.run(count).avg_rtt
