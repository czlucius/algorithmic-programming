# A rock B paper C scissor
# X      Y paper Z
totalscore = 0
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        score = 0
        moves = line.split(" ")
        o = {"A": 1, "B": 2, "C": 3}
        opp = o[moves[0].strip()]
        m = {"X": 1, "Y":2, "Z": 3}
        mine = m[moves[1].strip()]
        if mine == opp:
            score += mine
            score += 3
        elif ((opp == 1 and mine == 2) or (opp == 2 and mine == 3) or (opp == 3 and mine == 1)):
            score += mine
            score += 6
        else:
            score += mine
            
            
    
        totalscore += score     
        
print("Total score", totalscore)