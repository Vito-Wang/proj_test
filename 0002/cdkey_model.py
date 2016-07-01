# coding=utf-8
# show me the code 0002题， 把0001题生成的激活码写入mysql关系数据库
import mysql.connector


def cdkey_sql(filepath):
    # 建立数据库链接，设置游标，创建cdekys，如果表cdkeys存在，就删除表
    conn = mysql.connector.connect(user='root', password='199198', database='test', use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('drop table if exists cdkeys')
    cursor.execute('create table cdkeys  (id int not null auto_increment primary key, cdkey varchar(14))')

    # 首先把文件数据读入list中，遍历，去除空行，最后添加到数据库中
    with open(filepath, 'rb') as f:
        for i in f.readlines():
            result = i.strip()
            cursor.execute('insert into cdkeys (cdkey) values (%s)', [result])
    conn.commit()
    cursor.close()

    # 查询是否插入成功
    cursor = conn.cursor()
    cursor.execute('select * from cdkeys')
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    print values


if __name__ == '__main__':
    cdkey_sql('E:/data1.txt')
