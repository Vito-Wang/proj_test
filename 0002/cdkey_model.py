# coding=utf-8
import mysql.connector


def cdkey_sql(filepath):
    conn = mysql.connector.connect(user='root', password='199198', database='test', use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('drop table if exists cdkeys')
    cursor.execute('create table cdkeys  (id int not null auto_increment primary key, cdkey varchar(14))')
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
