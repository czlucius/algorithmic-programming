# A rock B paper C scissor
# X lose Y draw Z win
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
        if mine == 2:
            score += opp
            score += 3
        elif mine == 3:
            play = (opp % 3) + 1
            score += play
            score += 6
        elif mine == 1:
            play = ((opp+1) %3) + 1
            score += play  
            
    
        totalscore += score     
        
print("Total score", totalscore)