import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer, MultiprocessFTPServer, ThreadedFTPServer
from django.core.management import BaseCommand


def ftpServer(self, *args, **options):
    """
    实现主要逻辑,启动ftp服务
    :param args:
    :param options:
    :return:
    """
    authorizer = DummyAuthorizer()
    handler = FTPHandler
    handler.authorizer = authorizer
    authorizer.add_anonymous('/data/ftp/export/dbExpfiles')
    address = ('', 2121)
    server = ThreadedFTPServer(address, handler)
    # server = ThreadedFTPServer((FTP_IP, FTP_POST), handler)
    server.serve_forever()

if __name__ == '__main__':
    ftpServer()