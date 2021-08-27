def how2sum(target, arr):
    table = [None]*(target + 1)
    table[0] = []
    i = 0
    while i <= target:
        if table[i] is not None:
            for num in arr:
                if (i + num) < (target + 1):
                    table[i + num] = table[i] + [num]
        i += 1
    return table[target]


print(how2sum(7, [2, 4]))
print(how2sum(10, [2, 4, 5]))
print(how2sum(7, [2, 4, 3]))
