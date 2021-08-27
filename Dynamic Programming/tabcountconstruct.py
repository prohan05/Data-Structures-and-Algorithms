def countconstruct(target, arr):
    k = len(target)
    table = [0]*(k + 1)
    table[0] = 1
    for i in range(k + 1):
        if table[i] >= 1:
            for word in arr:
                if target[i:i + len(word)] == word:
                    table[i + len(word)] += 1
    return table[k]


print(countconstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(countconstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
