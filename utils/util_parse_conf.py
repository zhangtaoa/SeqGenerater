# coding=utf-8

# Copyright (c) 2018 - <tao.zhang@moji.com>

"""
Author: tao.zhang
Create Date: 2019/3/29
@Software: PyCharm
descirption:
"""
import configparser


class ParseIni(object):
    def __init__(self, filename=None):
        assert filename, "Filename Not Set"
        self.filename = filename

    def __enter__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)

        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == "__main__":
    with ParseIni("/Users/tao.zhang/PycharmProjects/SeqGenerater/config/seq.ini") as conf:
        print(conf.get("redis", "port"))
        print(conf.get("redis", "password", vars={"password": "aaaaaa"}))



