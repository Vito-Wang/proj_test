# -*- coding:utf-8 -*-
# 第0001题，生成200个激活码，激活码由26个大写字母和10个数字组合生成，长度为12位，不能重复，激活码中的字符可以重复

import random, string


def create_cdkey(num, lenth):
    """
    num: the cdkey num
    lenth: the cdkey lenth
    :param num:
    :param lenth:
    :return:
    """
    cdkey_collect = list(string.ascii_uppercase)
    for i in range(0,10):
        cdkey_collect.append(str(i))
    result = {}
    if  len(result) < num:
