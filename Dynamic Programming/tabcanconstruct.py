def canconstruct(target, arr):
    k = len(target)
    table = [False]*(k + 1)
    table[0] = True
    for i in range(k + 1):
        if table[i] is True:
            for word in arr:
                if target[i:i + len(word)] == word:
                    table[i + len(word)] = True
    return table[k]


print(canconstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(canconstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
