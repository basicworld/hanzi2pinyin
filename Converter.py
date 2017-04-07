# coding:utf8
"""
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re


class Converter(object):
    def __init__(self, dict_file='./pinyin_dict.txt'):
        self._dict = {}
        for line in open(dict_file):
            line = line.decode("utf-8").rstrip()
            self._dict[line[0]] = line[1:].split(',')

    def convert(self, string, jointer=',', with_tone=True, char_for_not_hanzi='XX0'):
        string = string.decode("utf-8")
        pinyin = []
        # map 层
        for key in string:
            pinyin.append(self._dict.get(key, [char_for_not_hanzi])[0])

        # 输出层
        if with_tone:
            return jointer.join(pinyin)
        else:
            return jointer.join([i[:-1] for i in pinyin])
