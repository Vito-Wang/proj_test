# -*- coding:utf-8 -*-
# 第0001题，生成200个激活码，激活码由26个大写字母和10个数字组合生成，长度为12位，不能重复，激活码中的字符可以重复
# 生成器版本

import random
import string


def create_cdkey(num, lenth):
    """
    num: the cdkeys number
    lenth: the cdkey lenth
    :param num:
    :param lenth:
    :return:
    """
    cdkey_collect = list(string.ascii_uppercase)
    for i in range(0, 10):
        cdkey_collect.append(str(i))
    result = {}
    while len(result) < num:
        key = ''
        for index in range(lenth):
                key += (random.choice(cdkey_collect))
        if key in result:
            pass
        else:
            result[key] = 1
            yield key

    # for key in result:
    #     print key


if __name__ == '__main__':
    for k in create_cdkey(200, 12):
        print k


