"""
def gridTrav(m,n):
    if m == 1 and n ==1:
        return 1
    elif m==0 or n==0:
        return 0
    return gridTrav(m-1,n) + gridTrav(m, n-1)


print(gridTrav(3,3))
"""


def gridtrav(m, n):
    dicto = {}
    key = m, n
    if key in dicto.keys():
        return dicto[key]
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    dicto[key] = gridtrav(m - 1, n) + gridtrav(m, n - 1)
    return dicto[key]


print(gridtrav(3, 3))
