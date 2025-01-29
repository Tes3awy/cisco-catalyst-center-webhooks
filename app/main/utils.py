# -*- coding: utf-8 -*-
import os
import socket

from dotenv import load_dotenv

load_dotenv(".flaskenv")


def is_server_running():
    primary_ip = socket.gethostbyname_ex(socket.getfqdn())[2][1]
    try:
        sock = socket.create_connection(
            (primary_ip, os.getenv("FLASK_RUN_PORT", 5443)), timeout=3
        )
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False
    else:
        sock.close()
        return True
