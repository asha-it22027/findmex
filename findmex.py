n = int(input())
arr = list(map(int, input().split()))

visited = [-1] * (n + 2)
mex = 0
result = []

for i in range(n):
    num = arr[i]
    visited[num] = 1
    while visited[mex] != -1:
        mex += 1
    result.append(mex)

for r in result:
    print(r, end=" ")