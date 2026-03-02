high_scores = [100, 90, 80, 70, 60]
current_score = 85
if high_scores:
    for high_score in high_scores:
        if current_score > high_score:
            print(f"Congratulations! You have a new high score of {current_score}!")
            break
else:
    print("No high scores yet. Be the first to set a high score!")