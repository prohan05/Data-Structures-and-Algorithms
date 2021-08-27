"""
def allconstruct(target, arr):
    if target == '':
        return [[]]
    result = []
    for i in range(len(arr)):
        if str(arr[i]) == target[:len(str(arr[i]))]:
            suffix = allconstruct(target[len(arr[i]):], arr)
            for x in suffix:
                result += [[arr[i]] + x]

    return result
"""


def allconstruct(target, arr, memo={}):
    if target in memo:
        return memo[target]
    elif target == '':
        return [[]]
    result = []
    for i in range(len(arr)):
        if str(arr[i]) == target[:len(str(arr[i]))]:
            suffix = allconstruct(target[len(arr[i]):], arr, memo)
            for x in suffix:
                result += [[arr[i]] + x]
    memo[target] = result
    return result


print(allconstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(allconstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
