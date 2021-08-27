list1 = [22, 75, 332, 44, 876, 12, 87, 55, 90, 33]
list2 = [12, 22, 33, 44, 55, 75, 87, 90, 332, 876]


def is_sorted(list):
    # for i in range(0, len(list)-1):
     #   if list[i] > list[i+1]:
      #      return False
    return all(list[i] <= list[i+1] for i in range(len(list)-1))
    #return True


print(is_sorted(list1))
print(is_sorted(list2))
