# coding:utf-8
# 第0004题，统计英文文本中单词出现的个数（我的理解是统计其中某个单词出现的个数，看了下大家的解答，都是统计全部的英文单词）
# 下面的解答是统计全部的英文字母个数
# 如果是统计某个单词的个数，可以先读取文件到list， 再count某个单词的个数

import re


def count(filepath):
    with open(filepath, 'rb') as f:
        # 读取文件到字符串s
        s = f.read()
        # 通过正则匹配，将s转换为含有全部英文文本的list
        words = re.findall(r'[a-zA-Z0-9]+', s)
        return len(words)

if __name__ == '__main__':
    num = count('C:\Users\wwd\Desktop\English.txt')
    print num
