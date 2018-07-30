#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import redis

class MyRedis:
    '''
    Redis连接工具
    '''

    def __init__(self, host='localhost', port=6379, password=None):
        self.host = host
        self.port = port
        self.password = password
        self.connect_pool = None

    def get_connect_pool(self):
        '''
        获取数据库连接池
        '''
        if (not self.connect_pool):
            self.connect_pool = redis.ConnectionPool(host=self.host, port=self.port, password=self.password)
        return self.connect_pool

    def get_redis(self, db=0):
        '''
        获取redis连接
        '''
        # 当连接池为空时，创建连接池
        if (not self.connect_pool):
            self.get_connect_pool()
        return redis.Redis(connection_pool=self.connect_pool, db=db)

    def get_pipe(self, db=0):
        '''
        获取管道,可一次请求多条命令
        '''
        r = self.get_redis(self, db=db)
        return r.pipeline()


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class redisUtli:
    '''
    使用装饰器构造单例模式,Redis操作工具类
    '''
    
    def set(connect, key, value):
        connect.set(key, value)

