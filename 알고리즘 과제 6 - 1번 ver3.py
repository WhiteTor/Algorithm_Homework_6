n = int(input())

arr_start = []
arr_end = []
max = 0

for _ in range(n):
    a, b = map(int, input().split())
    arr_start.append(a)
    arr_end.append(b)

for i in range(n):
    start = arr_start[i]
    end = arr_end[i]
    for j in range(start, end + 1):
        count = 0
        for k in range(n):
            if arr_start[k] <= j and arr_end[k] >= j:
                count += 1
        if count > max:
            max = count
                

print(max)