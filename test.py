# coding:utf8
"""
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


if __name__ == '__main__':
    string = ['大中国', '博大精深', '今始科技', 'sdafew', '12d0--0;/']
    from Converter import Converter
    con = Converter()
    for i in string:
        print i, con.convert(i)
        print i, con.convert(i, with_tone=False)
