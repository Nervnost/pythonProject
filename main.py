n = 9
matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * n
x = 0
y = 0
z = 1

for x in range(n-1):
    matrix[0][x] = z
    z +=1
for y in range(n-1):
    matrix[y][n-1] = z
    z +=1
for x in range(n-1):
    matrix[n-1][n-1-x] = z
    z += 1
for y in range(n-1):
    matrix[n-1-y][0] = z
    z += 1
for a in matrix:
    print(a)
