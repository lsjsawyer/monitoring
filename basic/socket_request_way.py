# -*- coding: utf-8 -*-
import socket


def socket_get_way(host, port, socket_package):
    BufferSize = 1024 * 1000
    coon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    coon.connect((host, port))
    coon.sendall(socket_package.encode('utf8'))
    receive_data = coon.recv(BufferSize)
    return receive_data