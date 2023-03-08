# -----------------
# Communications for S7-1200 UDP
# by Radosław Tecmer
# radek69tecmer@gmail.com
# --------------------

from socket import socket, AF_INET, SOCK_DGRAM
import struct
import time
from binascii import hexlify


def send(command, position):
    cpu = ('192.168.1.121', 3000)
    pc = ('192.168.1.10', 3000)
    with socket(AF_INET, SOCK_DGRAM) as sock:
        sock.bind(pc)
        data = struct.pack('!HI', command, position)
        print('Binary Data:', hexlify(data).decode())
        sock.send(data, cpu)
        data = sock.recv(1024)
        return  struct.unpack('!HI', data)


def incr_gen(start, stop, incr):
    yield from range(start, stop + 1, incr)


if __name__ == '__main__':
    gen = incr_gen(20, 200, 5)
    for pos in gen:
        print('Sending:', 1, pos)
        send(1, pos)
        time.sleep(1)

