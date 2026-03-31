import pandas as pd
import seaborn as sns
import time
#현재문제 : Single responsibility 위배 + Open closed prinsiple 위해
# 해결 -> 시간 출력 빼기 + 새로운 함수 만들기

def time_measure_decorator(f): # 이런 함수형 코드를 데코레이터 패턴이라고 한다
    def wrapper(*args):
        s = time.time()
        r = f(*args)
        e = time.time()
        print(e-s)
        return r
    return wrapper


@time_measure_decorator
def one_to_n_loop(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result

@time_measure_decorator
def one_to_n_math(n):
    r= n*(n+1)//2
    return r

number = int(input("input number :"))
print(one_to_n_loop(number))
print(one_to_n_math(number))