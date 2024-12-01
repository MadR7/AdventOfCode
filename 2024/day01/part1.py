import heapq

left_numbers = []
right_numbers = []

with open('sample.txt', 'r') as f:
    for line in f:
        parts = line.split()
        if len(parts) == 2:
            left, right = map(int, parts)
            left_numbers.append(left)
            right_numbers.append(right)


heapq.heapify(left_numbers)
heapq.heapify(right_numbers)

sum = 0
for i in range(len(left_numbers)):
    sum += abs(heapq.heappop(left_numbers) - heapq.heappop(right_numbers))

print(sum)