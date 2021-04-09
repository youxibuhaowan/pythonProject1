"""
Time:2021/4/8 16:05
Author:中庸猿
奋斗不止，赚钱不停    
"""
from multiprocessing import Pool
from queue import Queue
import time

if __name__ == '__main__':
    with Pool(maxtasksperchild=2) as pool:
        while True:
            try:
                q = Queue()

                    """  
                     一个进程进行数据库的写
                        多线程从tushare中读取，并写入数据
                    
                    一个进程执行数据的读，并渲染到echarts
                        多线程读取信息，多线程渲染数据
                    """
                    # 读取tushare信息进行数据库写入
                    pool.apply_async()

                    # 读取数据库，将数据进行渲染
                    # 使用队列，每次数据每个数据进行完成就进行渲染
                    pool.apply_async(, args=(q,))
            except:
                print('Error')
            finally:
                pool.close()

            # 每60s刷新一次数据
            time.sleep(60)