# countdown recursion
"""
def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print("T minus", x)
        print("oompa loompa")
        countdown(x-1)
        print("bada bing bada bing")

countdown(5)
"""


def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr - 1)


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print("{} to thr power of {} is {}".format(5, 3, power(5, 3)))
print("{} to thr power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))

