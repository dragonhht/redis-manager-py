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

    def get_db_size(self):
        '''
        获取数据库数量
        '''
        r = self.get_redis()
        dbs = r.config_get('databases')
        return int(dbs['databases'])

    def get_db_keys(self, db):
        '''
        获取数据库的所有键
        '''
        r = self.get_redis(db=db)
        return r.keys('*')

    def get_key_type(self, key):
        '''
        获取键的类型
        '''
        r = self.get_redis()
        return bytes.decode(r.type(key))

    def get_key_ttl(self, key):
        '''
        获取ttl
        '''
        r = self.get_redis()
        ttl = r.ttl(key)
        if (ttl):
            return ttl
        else:
            return -1

    def set_key_ttl(self, key, ttl):
        '''
        设置ttl
        '''
        r = self.get_redis()
        if (ttl == -1):
            r.persist(key)
        else:
            r.expire(key, ttl)


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

if __name__ == '__main__':
    my_redis = MyRedis()
    print(my_redis.get_key_ttl('test'))
