# coding: utf-8

import string


def parse_price(price):
    '''
    把输入变成整数保存, 输入可以是'1.22', 也可以是1.22,
    或者100.00, 100之类的
    '''
    if isinstance(price, basestring):
        try:
            price = string.atof(price)
        except ValueError:
            return 0
    if not isinstance(price, (int, float)):
        return 0
    return int(price*100)


def to_price(price):
    '''
    把输入变成可以显示的价格.
    输入必须是一个整数, 数据库里的要求.
    '''
    if not isinstance(price, int):
        return '0.00'
    return str(price/100.0)
