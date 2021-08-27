"""

def cansum(arr, n):
    length = len(arr)
    for i in range(0, length):
        for j in range(i+1, length):
            if arr[i] + arr[j] == n:
                return True
            else:
                return False

print(cansum([5, 3, 4, 7], 7))
"""

"""
def cansum(arr, n, dicto= {}):

    if n in dicto.keys():
        return dicto[n]
    elif n == 0:
        return True
    elif n < 0:
        return False
    for i in arr:
        subd = n - i
        if cansum(arr,subd, dicto) is True:
            dicto[n] = True
            return True
    dicto[n] = False
    return False


print(cansum([5, 3, 4, 7], 100))
"""
"""
# Doesn't work

def is2sum(target, arr):
    if target == 0:
        return True
    elif target < 0:
        return False
    for num in arr:
        remainder = target - num
        if is2sum(remainder, arr) is True:
            return True
    else:
        return False


print(is2sum(7, [2, 3]))
print(is2sum(4, [2, 2]))

"""


def is2sum(target, arr):
    memo = {}

    for i in range(len(arr)):
        if (target - arr[i]) in memo:
            return True
        else:
            memo[arr[i]] = i
    return False


print(is2sum(7, [2, 3]))
print(is2sum(4, [2, 2]))
print(is2sum(11,[5, 3, 4, 7]))

"""
   def twoSum(self, nums, target):
      
      required = {}
      for i in range(len(nums)):
         if target - nums[i] in required:
            return [required[target - nums[i]],i]
         else:
            required[nums[i]]=i
"""
