def count_letters(text):
  count = 0
  for char in text:
    if char.isalpha():
      count+= 1
  return count
print("Greetings! I am C3PO, human-cyborg relations.")
name = input("May I ask what your name is? ")
print(f"Ah, yes, Master {name}. What is on your mind?")

# variables
go_aways = 0
total_letters = 0

# convo loop
while True:
  user_input = input()
  validate = user_input.lower()
  total_letters += count_letters(user_input)
  if "go away" in validate:
    go_aways += 1
    if go_aways == 1:
      print(f"Hang on tight, Master {name}. You’ve got to come back. You wouldn’t want my life to get boring, would you?")
    elif go_aways >= 2:
      print(f"Master {name}, go that way! You have used {total_letters} in our chat today. You’ll be malfunctioning within a day, you nearsighted scrap pile. And don’t let me catch you following me, begging for help, because you won’t get it!")
      break
  elif "r2d2" in validate:
    print("R2D2, he should know better than to trust a strange computer!")
  elif "millennium falcon" in validate:
    print("Sir, the possibility of successfully navigating an asteroid field is approximately 3,720 to 1.")
  elif validate.startswith("i feel"):
    print(f"When I feel that way…well droids don’t feel. Master {name}, it’s why nobody worries about upsetting a droid.")
  elif validate.startswith("i am"):
    something = user_input[5:].strip()
    print(f"When I was last {something} I suggested a new strategy to R2: to let the Wookiee win.")
  elif user_input.endswith("?"):
    print(f"For a mechanic, you seem to do an incessant amount of thinking {name}. If I told you half the things I've heard about this Jabba the Hutt, you'd probably short circuit.")
  elif user_input.endswith("!"):
    print(f"Sometimes I just don’t understand human behavior, {name}! After all, I’m only trying to do my job. What else?")
