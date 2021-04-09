"""
Time:2021/4/8 16:19
Author:中庸猿
奋斗不止，赚钱不停    
"""
import tushare as ts
import pymysql

# tushareToken
# ts.set_token('c43d43d2f232eba8a6c58928cb248be964fb271fa3ab48d2b9a60d40')
#
#
# # 获取tusahre传递的参数
# def get_tushare_data():
#     pass
#
#
# pro = ts.pro_api()

# df = pro.trade_cal(exchange='', start_date='20180901',
#                    end_date='20181001',
#                    fields='exchange,cal_date, is_open, pretrade_date',
#                    is_open='0')
# print(df)

a = 'select stu_id from tb_student;'

# 第一步: 创建链接对象
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='admin', password='123456',
                       database='tushare', charset='utf8mb4')
try:
    # 第二步: 获取游标对象
    with conn.cursor() as cursor:
        # 第三步: 通过游标对象向数据库服务器发出SQL语句
        # cursor.execute('SQL语句')
        affected_rows = cursor.execute(
           # 数据库语言
            'call tushare.new_select;'
        )
        if affected_rows == 1:

            print('新增部门成功')

    # 第四部: 通过链接对象提交事务
    conn.commit()
except pymysql.MySQLError as err:
    print(err)
    conn.rollback()
finally:
    # 第五步: 关闭连接释放资源
    conn.close()
