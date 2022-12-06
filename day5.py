import re

with open('inputs/day5.txt', 'r') as f:
    lines = f.read().splitlines()

containers = {}    

#Grab the setup lines - the letters are at the same positions so setup containers using position
match_iter = [re.finditer(r'[A-Z]', x) for x in lines[0:8]]

#Iterate through found letters and append to dictionary of lists
for matches in match_iter:
    for match in matches:
        if match.start() in containers:
            containers[match.start()].append(match.group())
        else:
            containers[match.start()] = [match.group()]

#Remap dictionary to 1-9 for ease of next step
#Each list of crates runs from top to bottom
container_tracker = {} 

for idx, x in enumerate(sorted(containers.keys())):
    container_tracker[idx+1] = containers[x]

#Move function
def process_move(move_command, reverse = True):
    count, source, target = [int(x) for x in re.findall(r'\b\d+\b', move_command)]
       
    #Reverse moved containers
    to_move = container_tracker[source][:count]
    if reverse:
        to_move.reverse()
    
    #Slice to get remaining containers on source stack
    container_tracker[source] = container_tracker[source][count:]
    
    #Append moved containers to start of target list (aka top)
    container_tracker[target] = to_move + container_tracker[target]

#Make the moves for part one
for line in lines[10:]:
    process_move(line)
    
for container in container_tracker.values():
    print(container[0])
    
print ('')

#Reset containers to start
for idx, x in enumerate(sorted(containers.keys())):
    container_tracker[idx+1] = containers[x]
    
for line in lines[10:]:
    process_move(line, reverse = False)

for container in container_tracker.values():
    print(container[0])
