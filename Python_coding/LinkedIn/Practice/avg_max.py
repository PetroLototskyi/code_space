def find_winner(player_scores):
    # Your code goes here
    highest_score=0
    winner=""

    for name, scores in player_scores.items():
        # print(name)
        # print(scores)
        avg=sum(scores)/len(scores)
        # print(avg)
        if avg>highest_score:
            highest_score=avg
            winner=name

    
    return [winner, highest_score]

player_scores = {
    'Arthur': [85, 90, 92],
    'Bela': [75, 80, 85],
    'Carol': [90, 92, 95],
    'Deepak': [87, 89, 91]
}
result = find_winner(player_scores)
print(result)