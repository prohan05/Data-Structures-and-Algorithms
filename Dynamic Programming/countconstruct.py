def countconstruct(target, arr, memo={}):
    j = 0
    if target in memo:
        return memo[target]
    elif target == '':
        return 1
    for i in range(len(arr)):
        s = str(arr[i])
        if s == target[:len(s)]:
            rest = target.replace(s, '')
            suffix = countconstruct(rest, arr, memo)
            j += suffix

    memo[target] = j
    return j


print(countconstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countconstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countconstruct('eeeeeef', ['e', 'ee', 'eee', 'f']))
