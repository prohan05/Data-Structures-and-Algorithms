items =[12, 22, 33, 44, 55, 75, 87, 90, 332, 876]


def binary(item, list):
    size = len(list) - 1
    lower = 0
    upper = size

    while lower <= upper:

        mid = (lower + upper)//2
        if list[mid] == item:
            return mid

        if item > list[mid]:
            lower = mid + 1
        else:
            upper = mid - 1
        pass

    if lower > upper:
        return None


print(binary(44, items))
print(binary(876, items))
print(binary(2223, items))
