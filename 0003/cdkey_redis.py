# coding=utf-8
# show me the code 0003题，将生成的激活码存入redis非关系型数据库
# author:vito-wang

import redis


def cdkey_redis(filepath):
    # 首先链接redis数据库，清空db内数据
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    r.flushdb()
    '''
     建立管道（管道是redis在提供单个请求中缓冲多条服务器命令的基类的子类。
     它通过减少服务器-客户端之间反复的TCP数据库包，从而大大提高了执行批量命令的功能。
     在此只是试用一下!
    '''
    p = r.pipeline()

    # 执行存储操作，最后打印出激活码
    with open(filepath, 'rb') as f:
        for i in f.readlines():
            result = i.strip()
            p.sadd('myset:cdkey', [result])
        else:
            p.execute()

    print (r.smembers('myset:cdkey'))


if __name__ == '__main__':
    cdkey_redis('E:/data1.txt')
