# if m,n => 3,6 it gave 4 sub arrays(no. of rows) of 7 elements(no. of columns)
def gridtab(m, n):
    table = [[0 for i in range(n+1)] for j in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j < n:
                table[i][j+1] += current
            if i < m:
                table[i+1][j] += current

    return table[m][n]


print(gridtab(3, 3))
