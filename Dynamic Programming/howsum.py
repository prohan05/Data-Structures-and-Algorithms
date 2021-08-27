"""
def howsum(target, arr):
    if target == 0:
        return []
    elif target < 0:
        return 'null'
    for num in arr:
        rem = target - num
        rem_result = howsum(rem, arr)
        if rem_result is not 'null':
            return rem_result + [num]
    return 'null'
"""

"""
def howsum(target, arr):
    memo = {}
    for i in range(len(arr)):
        if (target - arr[i]) in memo:
            return [memo[target - arr[i]], arr[i]]
        else:
            memo[arr[i]] = arr[i]
"""


def howsum(target, arr, memo={}):

    if target in memo:
        return memo[target]
    elif target == 0:
        return []
    elif target < 0:
        return None
    for i in range(len(arr)):
        rem = target - arr[i]
        rem_result = howsum(rem, arr, memo)
        if rem_result is not None:
            memo[target] = rem_result + [arr[i]]
            return memo[target]

    memo[target] = None
    return None


print(howsum(7, [2, 3]))
print(howsum(7, [5, 4, 3, 7]))
print(howsum(8, [2, 3, 5]))
print(howsum(300, [7, 14]))
print(howsum(7, [2, 4]))
