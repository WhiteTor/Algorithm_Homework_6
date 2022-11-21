n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())

    arr.append((a, 'start'))
    arr.append((b, 'end'))

arr.sort(key = lambda x : (-ord(x[1][0]), x[0]))

for i in range(n):
    if arr[i][1] == 'start':


#for i in range(n):