def name():
    print(123456)

name()

# 阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))
