def fibtab(n):
    fibtablo = [0]*(n+1)
    fibtablo[0] = 0
    fibtablo[1] = 1
    for i in range(2, n+1):
        fibtablo[i] = fibtablo[i-1] + fibtablo[i-2]
    return fibtablo[n]


print(fibtab(6))