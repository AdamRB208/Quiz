
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