"""Ping utility module.
"""

__author__ = 'Volodymyr Burenin'

import os
import random
import select
import socket
import struct
import time


def calc_crc16(data):
    """Calc byte string CRC16"""
    s = 0
    if len(data) % 2 == 1:
        data += chr(0)

    for i in range(0, len(data), 2):
        if type(data[i]) is str:
            s += ord(data[i]) + (ord(data[i + 1]) << 8)
        else:
            s += data[i] + (data[i + 1] << 8)
        s &= 0xffffffff

    s = (s >> 16) + (s & 0xffff)

    s = ~s & 0xffff
    return s >> 8 | (s << 8 & 0xff00)


def receive_reply(raw_socket, wait_timeout):
    """ICMP echo reply.
    """

    select_data = select.select([raw_socket], [], [], wait_timeout)
    recv_ts = time.time()

    if select_data[0]:
        packet, addr = raw_socket.recvfrom(1024)

        # Cut IP header.
        ip = packet[0] if type(packet[0]) is int else ord(packet[0])
        ip_len = (ip & 0xf) * 4
        icmp_header = packet[ip_len:ip_len + 8]

        icmp_t, icmp_c, crc16, pkt_id, seq = struct.unpack(
            '>bbHHH', icmp_header)

        if icmp_t == 0 and icmp_c == 0:
            return pkt_id, seq, recv_ts

    return None, None, None


def send_ping(raw_socket, dest_addr, pkt_id, seq_code, data_length=48):
    """Echo request.
    """

    pkt_crc16 = 0
    # icmp_type(1B):icmp_code(1B):crc16(2B):id(2):seq(2b)
    header = struct.pack('>bbHHH', 8, 0, pkt_crc16, pkt_id, seq_code)

    data = b'p' * data_length

    pkt_crc16 = calc_crc16(header + data)
    header = struct.pack('>bbHHH', 8, 0, pkt_crc16, pkt_id, seq_code)

    packet = header + data
    raw_socket.sendto(packet, (dest_addr, socket.MSG_OOB))


def ping(host, timeout=2, ping_id=None, udp=False):
    """Ping remote host.

    :param str host: Host name/address.
    :param float timeout: timeout.
    :param int ping_id: 16 bit integer to identify packet.
    """
    dest_addr = socket.gethostbyname(host)
    icmp = socket.getprotobyname('icmp')
    socket_type = socket.SOCK_DGRAM if udp else socket.SOCK_RAW
    raw_socket = socket.socket(socket.AF_INET, socket_type, icmp)

    ping_id = os.getpid() if ping_id is None else ping_id
    ping_id &= 0xffff

    seq_code = random.randint(1, 65535)

    latency = None

    start_ts = time.time()
    end_ts = start_ts + timeout

    send_ping(raw_socket, dest_addr, ping_id, seq_code)

    while time.time() < end_ts:
        r_ping_id, r_seq_code, r_recv_ts = receive_reply(raw_socket, timeout)
        if ping_id == r_ping_id and r_seq_code == seq_code:
            latency = r_recv_ts - start_ts
            break

    return latency

