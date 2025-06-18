def calcuclate_score(s):
    score = 0 
    for i in range(len(s)-1):
        print(f"{s[i]}-{ord(s[i])}")
        score = abs(ord(s[i]) - ord(s[i+1]))
    return score

s = "Allah"

print(calcuclate_score(s))