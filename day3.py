#Make a list of letters for priority score
import string

priority = list(string.ascii_lowercase + string.ascii_uppercase)

with open('inputs/day3.txt', 'r') as f:
    lines = f.read().splitlines()

#Since the two component halves have the same length and only one character in common...
#We can compare first half and second half in an one-liner split/set intersection

common_item = [list(set(x[0:len(x) // 2]).intersection(x[len(x) // 2:]))[0] for x in lines]

#Use letter list index (+1) as score
print(sum([priority.index(x) + 1 for x in common_item]))

#For task two - we just need the common intersection between three lines. Compartments don't matter
import numpy as np

badge_items = [list(set(x[0]).intersection(x[1]).intersection(x[2]))[0] for x in np.array_split(lines, len(lines) / 3)]
print(sum([priority.index(x) + 1 for x in badge_items]))
