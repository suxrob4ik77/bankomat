import  time,os
from threading import current_thread
from  multiprocessing import Process, current_process
from add import *
count=100_000_000


def read_file(add):
    p_id=os.getpid()
    print(f"{p_id}---{current_process().name}---{current_thread().name}---kutish boshlandi")
    with open(add,"r") as file:
        f=file.read()

        print(f"{p_id}---{current_process().name}---{current_thread().name}---kutish tugadi")
        return f


#
# def cpu_b(k):
#     p_id = os.getpid()
#     print(f"{p_id}---{current_process().name}---{current_thread().name}---hisoblash boshlandi")
#     while k>0:
#         k -=1
#     print(f"{p_id}---{current_process().name}---{current_thread().name}---hisoblash tugadi")


if __name__=="__main__":
    s_time=time.time()
    t1 = Process(target=read_file, args=("add.py",))
    t2 = Process(target=read_file, args=("add.py",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    e_time=  time.time()
    print("vaqt",e_time-s_time)

# 1 dan 100 gacha bugan massiv juft elementlari kopaytmasiga shu massifning toqlarini kopaytmasini ayirish