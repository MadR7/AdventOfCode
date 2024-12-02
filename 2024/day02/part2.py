# --- Part Two ---
# The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

# The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

# More of the above example's reports are now safe:

# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.
# Thanks to the Problem Dampener, 4 reports are actually safe!

# Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

def get_sign(a, b):
    if a < b:
        return 1
    elif a > b:
        return -1
    return 0

def is_safe(report):
    if len(report) < 2:
        return False
    is_increasing = True
    is_decreasing = True
    
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if diff > 3 or diff <= 0:
            is_increasing = False
        if diff < -3 or diff >= 0:
            is_decreasing = False
        if not is_increasing and not is_decreasing:
            return False
    return True

reports = []
with open('sample.txt', 'r') as f:
    for line in f:
        parts = line.split()
        if parts: 
            reports.append([int(x) for x in parts])
safe_count = 0
for report in reports:
    if is_safe(report):
        safe_count += 1
        continue
        
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            safe_count += 1
            break

print(safe_count)