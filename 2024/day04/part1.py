# --- Day 4: Ceres Search ---
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

# As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# The actual word search will be full of letters instead. For example:

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# Take a look at the little Elf's word search. How many times does XMAS appear?


def search(matrix, word, row, col, dx, dy, current_pos):
    if current_pos == len(word):
        return 1
    
    if (row < 0 or row >= len(matrix) or 
        col < 0 or col >= len(matrix[0]) or 
        matrix[row][col] != word[current_pos]):
        return 0
    
    return search(matrix, word, row + dx, col + dy, dx, dy, current_pos + 1)

def count_xmas(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    target = "XMAS"
    count = 0
    
    # All 8 directions: right, down-right, down, down-left, left, up-left, up, up-right
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    # Search from each cell as starting point
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                count += search(matrix, target, i, j, dx, dy, 0)
    
    return count

with open('input.txt', 'r') as f:
    matrix = []
    for line in f:
        row = list(line.strip())
        if row:
            matrix.append(row)

result = count_xmas(matrix)
print(result)