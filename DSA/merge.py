items = [32, 62, 18, 54, 99, 59, 80, 12, 44]


def merge(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while j < len(right):
            list[k] = list[j]
            j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1


print(items)
merge(items)
print(items)
