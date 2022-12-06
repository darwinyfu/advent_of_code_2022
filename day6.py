with open('inputs/day6.txt', 'r') as f:
    lines = f.read().splitlines()
    data_stream = lines[0] #Since it's just one string

#For each segment of four letters, get unique character count
#Print index of first occurrence of all unique (+ offset of 4)
marker_length = 4
print([len(set(data_stream[i:i + marker_length])) for i in range(len(data_stream) - marker_length)].index(marker_length) + marker_length)

#Part 2 just change marker to 14
marker_length = 14
print([len(set(data_stream[i:i + marker_length])) for i in range(len(data_stream) - marker_length)].index(marker_length) + marker_length)
