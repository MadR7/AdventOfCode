# The Elf looks quizzically at you. Did you misunderstand the assignment?

# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

# M.S
# .A.
# M.S
# Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

# Here's the same example from before, but this time all of the X-MASes have been kept instead:

# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# In this example, an X-MAS appears 9 times.

# Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?



with open('input.txt', 'r') as f:
    matrix = []
    for line in f:
        row = list(line.strip())
        if row:
            matrix.append(row)

count = 0
rowLength = len(matrix)
colLength = len(matrix[0])
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i + 2 < rowLength and j + 2 < colLength:
            if matrix[i+1][j+1] == 'A':
                if matrix[i][j] == 'M' and matrix[i+2][j+2] == 'S' or matrix[i][j]=='S' and matrix[i+2][j+2]=='M':
                    if matrix[i][j+2] == 'M' and matrix[i+2][j] == 'S' or matrix[i][j+2]=='S' and matrix[i+2][j]=='M':
                        count += 1
                

print(count)