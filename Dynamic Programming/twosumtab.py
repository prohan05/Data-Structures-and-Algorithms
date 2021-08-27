def twosumtab(target, arr):
    table = [False]*(target + 1)
    table[0] = True
    i = 0
    while i <= target:
        if table[i] is True:
            for num in arr:
                if (i + num) < (target+1):
                    table[i + num] = True
        i += 1
    return table[target]


print(twosumtab(7, [2, 4]))
