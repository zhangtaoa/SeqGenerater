# coding=utf-8

# Copyright (c) 2018 - <tao.zhang@moji.com>

"""
Author: tao.zhang
Create Date: 2019/3/29
@Software: PyCharm
descirption:
"""
import os
import time

from config.redis_key import RedisKey
from config.config import *
from utils.util_redis import ConnectionPool


class CreateSeq(object):

    def __init__(self, ):
        self.project_path = os.path.dirname(os.path.abspath(__file__))
        self.conf_instance = config["default" or "default"]
        self.r = ConnectionPool(**self.conf_instance.REDIS).r
        self.key = None

    def _gen_seq_key(self, key=None, **kwargs):

        if key is None:
            curr_key = "%s:%s" % (RedisKey.INCR_KEY,
                                  time.strftime(RedisKey.KEY_SUFFIX_FORMAT,
                                                time.localtime(time.time())))

            if self.key is not None and curr_key != self.key:
                self.clear_seq()

            self.key = curr_key

    # def set_seq(self, key=None, **kwargs):
    #     assert key, "key not set, must set"
    #     self._gen_seq_key(key, **kwargs)

    def get_seq(self):
        self._gen_seq_key()
        return "%ld%08d" % (time.time()*1000*1000, self.r.incr(self.key))

    def clear_seq(self):
        self._gen_seq_key()
        if self.key is not None and self.r.exists(self.key):
            self.r.delete(self.key)


if __name__ == "__main__":
    q = CreateSeq()
    i = 10
    # q.clear_seq()
    while i > 0:
        print(q.get_seq())
        i -= 1
