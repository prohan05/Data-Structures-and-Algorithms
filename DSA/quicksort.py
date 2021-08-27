items = [22, 75, 332, 44, 876, 12, 87, 55, 90, 33]


def quicksort(list1, first, last):
    if first < last:
        pivot_index = partition(list1, first, last)

        quicksort(list1, first, pivot_index - 1)
        quicksort(list1, pivot_index + 1, last)


def partition(list_values, first, last):

    pivot_value = list_values[first]

    lower = first + 1
    upper = last
    done = False
    while not done:
        while lower <= upper and list_values[lower] <= pivot_value:
            lower += 1
        while list_values[upper] >= pivot_value and upper >= lower:
            upper -= 1
        if upper < lower:
            done = True
        else:
            temp = list_values[lower]
            list_values[lower] = list_values[upper]
            list_values[upper] = temp

    temp = list_values[first]
    list_values[first] = list_values[upper]
    list_values[upper] = temp

    return upper


print(items)
quicksort(items, 0, len(items) - 1)
print(items)
