def allconstruct(target, arr):
    k = len(target)
    table = [[]]*(k + 1)
    table[0] = [[]]
    for i in range(k + 1):
        for word in arr:
            if target[i:i + len(word)] == word:
                new_comb =

    return table[k]


print(allconstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(allconstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
