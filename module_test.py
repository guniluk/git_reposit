#13_module_import.ipynb 예제에서 사용하는 모듈

def fibo(n):
    a, b = 0, 1
    while b < n:
        print(b, end ='**')
        a, b = b, a+b
    print('&&')

def fibo2(n):
    result=[]
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# print(fibo2(10))
# print(fibo(10))
