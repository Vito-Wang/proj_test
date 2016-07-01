# -*- coding:utf-8 -*-
# 第0001题，生成200个激活码，激活码由26个大写字母和10个数字组合生成，长度为12位，此版本激活码不重复，激活码中的字符可以重复
# 生成器的版本，程序有待改进

import random
import string


def create_cdkey(num, length):
    """
    num: the cdkeys number
    length: the cdkey length
    :param num:
    :param length:
    :return:
    """
    # 生成由26个大写字母和10个数字组成的列表，ascii_uppercase代表string中的大写字母。
    cdkey_collect = list(string.ascii_uppercase)
    for i in range(0, 10):
        cdkey_collect.append(str(i))
    result = {}
    # 生成num个激活码，激活码长度为length
    while len(result) < num:
        key = ''
        for index in range(length):
                key += (random.choice(cdkey_collect))
        if key in result:
            pass
        else:
            result[key] = 1
            yield key

    try:
        with open('E:/data1.txt', 'wb') as f:
            for k in create_cdkey(200, 12):
                f.writelines(k + '\n')

    except IOError, e:
        print 'IOError', e


if __name__ == '__main__':
    create_cdkey(200,12)

