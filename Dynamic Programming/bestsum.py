"""
def bestsum(target, arr):
    shortest_comb = None
    if target == 0:
        return []
    elif target < 0:
        return None
    for i in range(len(arr)):
        rem = target - arr[i]
        if bestsum(rem, arr) is not None:
            combination = bestsum(rem, arr) + [arr[i]]
            if shortest_comb is None or len(combination) < len(shortest_comb):
                shortest_comb = combination

    return shortest_comb

"""


def bestsum(target, arr, memo={}):

    shortest_comb = None
    if target in memo:
        return memo[target]
    elif target == 0:
        return []
    elif target < 0:
        return None
    for i in range(len(arr)):
        rem = target - arr[i]
        if bestsum(rem, arr) is not None:
            combination = bestsum(rem, arr, memo) + [arr[i]]
            if shortest_comb is None or len(combination) < len(shortest_comb):
                shortest_comb = combination

    memo[target] = shortest_comb
    return shortest_comb


print(bestsum(7, [5, 3, 4, 7]))
print(bestsum(8, [2, 3, 5]))
print(bestsum(8, [1, 4, 5]))
print(bestsum(100, [1, 2, 5, 25]))
