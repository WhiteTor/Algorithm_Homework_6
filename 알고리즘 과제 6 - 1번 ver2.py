import heapq

n = int(input())

arr = [0] * 200000
arr_heap = []

for _ in range(n):
	a, b = map(int, input().split())
	for i in range(a, b + 1):
		arr[i] += 1
		
for i in arr:
	heapq.heappush(arr_heap, (-i, i))

print(heapq.heappop(arr_heap)[1])