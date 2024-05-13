import random
def score(dice):
    total_score = 0
    for num in range(1, 7):
        count = dice.count(num)
        if count >= 3:
            if num == 1:
                total_score += 1000
            else:
                total_score += num * 100
            count -= 3
        if num == 1:
            total_score += count * 100
        elif num == 5:
            total_score += count * 50
    return total_score

resultaten = []
for _ in range(6):
    resultaten.append(random.randint(1, 6))
    
print(*resultaten) 
print("Score van de dobbelstenen:", score(resultaten))