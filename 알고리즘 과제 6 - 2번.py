n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key = lambda x : (x[0], x[1]))

selected = 0
pin = 0
temp_arr = [0]

for i in range(1, n):
    if arr[selected][1] >= arr[i][0]:
        temp_arr.append(i)
        if i == (n - 1):
            pin += 1
    else:
        selected = i
        pin += 1
        temp_arr = [selected]

print(pin)
