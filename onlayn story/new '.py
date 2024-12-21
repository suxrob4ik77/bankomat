import  time,os
from asyncio import sleep
from threading import current_thread
from  multiprocessing import current_process
from time import sleep
from iritabillar import *
count=100_000_000
sleep=5

def io_b(sec):
    p_id=os.getpid()
    print(f"{p_id}---{current_process().name}---{current_thread().name}---kutish boshlandi")
    time.sleep(sleep)
    print(f"{p_id}---{current_process().name}---{current_thread().name}---kutish tugadi")



def cpu_b(k):
    p_id = os.getpid()
    print(f"{p_id}---{current_process().name}---{current_thread().name}---hisoblash boshlandi")
    while k>0:
        k -=1
    print(f"{p_id}---{current_process().name}---{current_thread().name}---hisoblash tugadi")



if __name__=="__main__":
    s_time=time.time()
    # 1- single threed io_b vaqt 10.000927209854126
    # io_b(sleep)
    # io_b(sleep)
    # 2 vaqt 5.0020787715911865
    # t1=Thread(target=io_b,args=(sleep,))
    # t2 = Thread(target=io_b, args=(sleep,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # 3 vaqt 5.249534368515015
    # t1 = Thread(target=io_b, args=(count,))
    # t2 = Thread(target=io_b, args=(count,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # 4 vaqt vaqt 0.2809751033782959
    # t1=Process(target=cpu_b,args=(sleep,))
    # t2 = Process(target=cpu_b, args=(sleep,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # 5 vaqt 5.269191741943359 multiprogressing
    # t1 = Process(target=io_b, args=(count,))
    # t2 = Process(target=io_b, args=(count,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # 6 vaqt 3.854376792907715
    # t1 = Process(target=cpu_b, args=(count,))
    # t2 = Process(target=cpu_b, args=(count,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    e_time=  time.time()
    print("vaqt",e_time-s_time)