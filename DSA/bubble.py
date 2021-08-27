def bubble(list1):
    for i in range(len(list1)-1, 0, -1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp

        print("Current stat: ", list1)


def main():
    list2 = [3, 2, 5, 76, 2, 98, 23, 980]
    bubble(list2)
    print("Result: ", list2)


if __name__ == "__main__":
    main()
