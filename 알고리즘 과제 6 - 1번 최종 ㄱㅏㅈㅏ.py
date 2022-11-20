from collections import Counter
n = int(input())

arr = []

for _ in range(n):
	a, b = map(int, input().split())
	arr.append(a)
	arr.append(b)

counter = Counter(arr).most_common()
mostcommon = [counter[0][0]]

for i in range(n):
	if counter[i][0] != counter[i + 1][0]:
		break
	mostcommon.append(counter[i+1][0])

result = []

for j in range(len(mostcommon)):
	temp = 0
	for i in range(n):
		if arr[2 * i] != mostcommon[j] and arr[2 * i + 1] != mostcommon[j]:
			if arr[2 * i] <= mostcommon[j] and arr[2 * i + 1] >= mostcommon[j]:
				temp += 1
		else:
			temp += 1
	result.append(temp)


print(max(result))