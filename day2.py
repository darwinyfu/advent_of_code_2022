#A for Rock, B for Paper, and C for Scissors.
#X for Rock, Y for Paper, and Z for Scissors.

#Shape scores 1 for Rock, 2 for Paper, and 3 for Scissors)
#Win-Loss scores (0 if you lost, 3 if the round was a draw, and 6 if you won)

shape_scores = {'X' : 1, 'Y' : 2, 'Z' : 3}
outcome_scores = {'A' : {'X' : 3, 'Y' : 6, 'Z' : 0},
                 'B' : {'X' : 0, 'Y' : 3, 'Z' : 6},
                 'C' : {'X' : 6, 'Y' : 0, 'Z' : 3}}

with open('inputs/day2.txt', 'r') as f:
    lines = f.read().splitlines()
    
throws = [x.split() for x in lines] #Just to make the scoring lines more readable

print(sum([shape_scores[x[1]] + outcome_scores[x[0]][x[1]] for x in throws]))

#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
strategy_scores = {'X' : 0, 'Y' : 3, 'Z' : 6}
throw_scores = {'A' : {'X' : 3, 'Y' : 1, 'Z' : 2},
                 'B' : {'X' : 1, 'Y' : 2, 'Z' : 3},
                 'C' : {'X' : 2, 'Y' : 3, 'Z' : 1}}

print(sum([strategy_scores[x[1]] + throw_scores[x[0]][x[1]] for x in throws]))
