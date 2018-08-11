#!/usr/bin/python
# -*- coding: UTF-8 -*- 

class ConnectModel:
    '''
    连接的数据实体
    '''

    def __init__(self, host='localhost', port=6379, password=None):
        self.host = host
        self.port = port
        self.password = password

    def set_host(self, host):
        self.host = host

    def set_port(self, port):
        self.port = port

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password