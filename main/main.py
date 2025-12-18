
score = 0

questions = [
  {
    'question': "What is the largest Planet in the Solar System?",
    'options' : ['A) The Sun', 'B) Jupiter', 'C) Saturn', 'D) Earth'],
    'answer' : 'B'
  },
  {
    'question': "What piece of Venoms body can turn into a new symbiote?",
    'options' : ['A) His fingers', 'B) His eyes', 'C) His tongue', 'D) Any part of him'],
    'answer' : 'C'
  },
  {
    'question': "In StarWars C-3PO is fluent in how many forms of communication?",
    'options' : ['A) over 3 Million', 'B) 3 Thousand', 'C) 8 Thousand', 'D) over 6 Million'],
    'answer' : 'D'
  },
  {
    'question': "In StarWars what is the name of Poe Dameron's droid?",
    'options' : ['A) BB-8', 'B) C-3PO', 'C) R2 D2', 'D) BD-8'],
    'answer' : 'A'
  },
  {
    'question': "What does Tony Stark call his AI Assistant?",
    'options' : ['A) Casper', 'B) Janis', 'C) Gleebour', 'D) Jarvis'],
    'answer' : 'D'
  },
  {
    'question': "What planet has the largest volcano in the solar system?",
    'options' : ['A) Earth', 'B) Mars', 'C) Venus', 'D) Pluto'],
    'answer' : 'B'
  }
]

for question in questions:
  print(f"Question \n {question['question']}")
  for option in question['options']:
    print(f"Option {option}")
  users_input = input('A, B, C or D?  ').capitalize()
  print(f"users input {users_input.capitalize()}")
  print(f"correct answer {question['answer']}")

  if users_input.capitalize() == question['answer']:
    print(f"Good Job!!!")
    score += 1
    print(f"Your score is: {score}")
  else:
    print(f"You Suck!!!")

if score == len(questions):
  print(f"Great Job! You got all of the questions correct!")
elif score == len(questions) // 2:
  print(f"Nice try you got at least half of the questions correct!")
else:
  print(f"Nice try, keep practicing and try again!")
