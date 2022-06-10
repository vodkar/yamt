import socket


def get_current_network():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    net = s.getsockname()[0]
    s.close()
    return net
