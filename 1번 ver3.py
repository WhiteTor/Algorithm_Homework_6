n = int(input())

arr_num = []
arr_count = []
index_count = 0

for _ in range(n):
	a, b = map(int, input().split())
	for i in range(a, b + 1):
		if i not in arr_num:
			arr_num.append(i)
			arr_count.append(1)
		else:
			arr_count[arr_num.index(i)] += 1

print(max(arr_count))