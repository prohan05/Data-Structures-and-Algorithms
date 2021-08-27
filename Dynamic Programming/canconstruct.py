"""
def canconstruct(target, arr):
    if target == '':
        return True
    for i in range(len(arr)):
        s = str(arr[i])
        if s == target[:len(s)]:
            rest = target.replace(s, '')
            suffix = canconstruct(rest, arr)
            if suffix is True:
                return True
    return False
"""


def canconstruct(target, arr, memo={}):
    if target in memo:
        return memo[target]
    elif target == '':
        return True
    for i in range(len(arr)):
        s = str(arr[i])
        if s == target[:len(s)]:
            rest = target.replace(s, '')
            suffix = canconstruct(rest, arr, memo)
            if suffix is True:
                memo[target] = True
                return True
    memo[target] = False
    return False


print(canconstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canconstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canconstruct('eeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'f']))
