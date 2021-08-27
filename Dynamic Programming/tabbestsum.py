def bestsum(target, arr):
    table = [None]*(target + 1)
    table[0] = []
    i = 0
    while i <= target:
        if table[i] is not None:
            for num in arr:
                if (i + num) < (target + 1):
                    current = table[i] + [num]
                    if table[i + num] is None or len(table[i + num]) > len(current):
                        table[i + num] = current

        i += 1
    return table[target]


print(bestsum(7, [2, 4]))
print(bestsum(10, [2, 4, 5]))
print(bestsum(7, [2, 4, 3]))
