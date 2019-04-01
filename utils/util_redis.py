# coding=utf-8

# Copyright (c) 2018 - <tao.zhang@moji.com>

"""
Author: tao.zhang
Create Date: 2019/3/29
@Software: PyCharm
descirption:
"""
import redis
import logging


class ConnectionPool(object):
    def __init__(self, **kwargs):
        assert kwargs["host"], "No Set Host"
        assert isinstance(kwargs.get("port", None), int), "No Set Port"

        if kwargs.get("password", None) is None:
            logging.warning("No Set Password")

        self.pool = redis.ConnectionPool(**kwargs)
        print(self.pool)
        self.r = redis.Redis(connection_pool=self.pool)

    def __getattr__(self, item):
        if item not in self.__dict__:
            raise KeyError(item)
        return self[item]

    def close(self):
        if self.pool is not None:
            self.pool.disconnect()


if __name__=="__main__":
    c = ConnectionPool(**{"host": "localhost", "port": 6379}).r


