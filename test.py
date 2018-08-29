import time

def decorator(func):
    def wrapper(*args, **kwargs):
        print("列表参数",end=" ")
        print(args)
        print("字典参数",end=" ")
        print(kwargs)
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return wrapper

@decorator 
def func():
    time.sleep(0.8)

def sum(a,b,c):
    print(a+b+c)

func2=decorator(sum)

func2(1,2,3) # 函数调用
# 输出：0.800644397735595