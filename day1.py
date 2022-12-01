elf_loads = {}
elf_number = 1

with open('inputs/day1.txt', 'r') as f:
    lines = f.readlines()
    
for line in [x.replace('\n', '') for x in lines]:
    if line == '':
        elf_number += 1
    elif elf_number in elf_loads:
        elf_loads[elf_number] += int(line)
    else:
        elf_loads[elf_number] = int(line)

print(max(elf_loads.values()))

print(sum(sorted(elf_loads.values())[-3:]))
