
import time
def time_funcsiya(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Funksiyaning ishlash vaqti: {end_time-start_time}")
        return result
    return wrapper
@time_funcsiya
def massala(a,b):
    time.sleep(4)
    return a+b
massala(10,15)

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_recursive(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
n = 15
print(fibonacci_recursive(n))
#suxrobdan  19-dekabr