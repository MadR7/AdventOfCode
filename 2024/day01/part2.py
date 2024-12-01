from collections import Counter

left_numbers = []
right_numbers = Counter()



with open('sample.txt', 'r') as f:
    for line in f:
        parts = line.split()
        if len(parts) == 2:
            left, right = map(int, parts)
            left_numbers.append(left)
            right_numbers[right] += 1

similarity_score = 0

for left in left_numbers:
    similarity_score += left * right_numbers[left]

print(similarity_score)

