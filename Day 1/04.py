# hghest score

scores = {"Ram" : 90, "Sham" : 79, "Mohan": 98}

def high_score(scores):
    return max(scores, key = scores.get)
print(high_score(scores))