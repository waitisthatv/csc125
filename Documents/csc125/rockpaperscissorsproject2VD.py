import random

# the rules
rules = {"R": "S", "P": "R", "S": "P"}
names = {"R": "Rock", "P": "Paper", "S": "Scissors"}

# choices and scoring
user_counts = {"R": 0, "P": 0, "S": 0}
score = {"user": 0, "computer": 0, "tie": 0}
streak = 0
streak_winner = None

while True:
  user = input("Choose Rock (R), Paper (P), Scissors (S), or Quit (Q): ").upper()
  if user == "Q":
    break
  if user not in ["R", "P", "S"]:
    print("Invalid input. Try again.")
    continue

  user_counts[user] += 1

  # computer choices will adapt to the player
  most_chosen = max(user_counts, key=user_counts.get)
  freq = [k for k, v in user_counts.items() if v == user_counts[most_chosen]]
  if len(freq) > 1:  # No single preferred weapon
    computer = random.choice(["R", "P", "S"])
  else:
    # choose weapon that beats user's most used weapon
    for k, v in rules.items():
      if v == most_chosen:
        computer = k

  print(f"Computer chose {names[computer]}")

  # regretting my streak idea with this mess
  if user == computer:
    print("Tie!")
    score["tie"] += 1
    streak = 0
    streak_winner = None
  elif rules[user] == computer:
    print("You win!")
    score["user"] += 1
    if streak_winner == "user":
      streak += 1
    else:
      streak = 1
      streak_winner = "user"
    if streak == 3:
      print("Streak bonus! Extra point!")
      score["user"] += 1
  else:
    print("Computer wins!")
    score["computer"] += 1
    if streak_winner == "computer":
      streak += 1
    else:
      streak = 1
      streak_winner = "computer"
    if streak == 3:
      print("Computer streak bonus! Extra point!")
      score["computer"] += 1

# print the final scoreboard
print("Game Over!")
print(f"Your wins: {score['user']}, Computer wins: {score['computer']}, Ties: {score['tie']}")
print(f"Your choices: Rock={user_counts['R']}, Paper={user_counts['P']}, Scissors={user_counts['S']}")
input("Press Enter to exit.")
