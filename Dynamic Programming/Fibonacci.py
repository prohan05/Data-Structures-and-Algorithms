def fib(n):
    fibTable = [0] * (n + 1)
    fibTable[0] = 0
    fibTable[1] = 1
    for i in range(2, n + 1):
        fibTable[i] = fibTable[i - 1] + fibTable[i - 2]
    print(fibTable[n])


fib(200)
