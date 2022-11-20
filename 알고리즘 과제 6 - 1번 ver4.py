from collections import Counter
n = int(input())

arr_start = []
arr_end = []

for _ in range(n):
	a, b = map(int, input().split())
	arr_start.append(a)
	arr_end.append(b)

counter_start = Counter(arr_start).most_common()
counter_end = Counter(arr_end).most_common()

result = 0

if counter_start[0][1] > counter_end[0][1]:
	for i in range(n):
		if arr_start[i] <= counter_start[0][0] and arr_end[i] >= counter_start[0][0]:
			result += 1
else:
	for i in range(n):
		if arr_start[i] <= counter_end[0][0] and arr_end[i] >= counter_end[0][0]:
			result += 1

print(result)