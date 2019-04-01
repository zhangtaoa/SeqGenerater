# coding=utf-8

# Copyright (c) 2018 - <tao.zhang@moji.com>

"""
Author: tao.zhang
Create Date: 2019/4/1
@Software: PyCharm
descirption:
"""


class Config(object):
    pass


class Dev(Config):
    REDIS = {"host": "localhost", "port": 6379}


config = {
    "default": Dev
}