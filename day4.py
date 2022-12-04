with open('inputs/day4.txt', 'r') as f:
    lines = f.read().splitlines()

#Hacky split: convert commas to dashes then split to get [elf 1 start, elf 1 end, elf 2 start, elf 2 end]
    
elf_pair_ranges = [x.replace(',', '-').split('-') for x in lines]

#Don't need to write out ranges, just compare ends
def check_fully_contain(ranges):
    ranges = [int(x) for x in ranges]
    #elf 1 range contains elf 2 range
    if ranges[0] <= ranges[2] and ranges[1] >= ranges[3]:
        return 1
    #elf 1 range inside elf 2 range
    elif ranges[0] >= ranges[2] and ranges[1] <= ranges[3]:
        return 1
    else:
        return 0

print(sum([check_fully_contain(x) for x in elf_pair_ranges]))

#For part 2- just check the endpoints with an or instead
def check_overlap(ranges):
    ranges = [int(x) for x in ranges]
    
    #If elf 1 low is higher than elf 2 high or
    #elf 1 high is lower than elf 2 low then there can be no overlap
    if ranges[0] > ranges[3] or ranges[1] < ranges[2]:
        return 0
    else:
        return 1

print(sum([check_overlap(x) for x in elf_pair_ranges]))

