n = int(input())
matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * n
x = 0
y = 0
z = 1
run = 0
while (run<n):
    m=n-run
    for x in range(run, m):
        matrix[run][x] = z
        z += 1
    for y in range(run+1,m):
        matrix[y][n - 1-run] = z
        z += 1
    for x in range(m-2, run,-1):
        matrix[n - 1 - run][x] = z
        z += 1
    for y in range(m-1, run, -1):
        matrix[y][run] = z
        z += 1
    run += 1

for j in matrix:
    for k in j:
        print("{:4d}".format(k), end="")
    print()

