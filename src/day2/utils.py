def evaluate_match(opponent: str, own: str) -> 'int':

  if opponent not in ['A', 'B', 'C']:
    raise ValueError(f"Oponent cannot use the value {opponent}")
    return 0
  
  if own not in ['X', 'Y', 'Z']:
    raise ValueError(f"Cannot use option {own}")
    return 0
  
  ROCK = ['A', 'X']
  PAPER = ['B', 'Y']
  SCISSORS = ['C', 'Z']

  WIN = 6
  LOSE = 0 
  DRAW = 3

  if opponent in ROCK:
      if own in ROCK:
         return DRAW
      if own in PAPER:
         return WIN
      if own in SCISSORS:
         return LOSE
      
  if opponent in PAPER:
     if own in ROCK:
        return LOSE
     if own in PAPER: 
        return DRAW
     if own in SCISSORS:
        return WIN
     
  if opponent in SCISSORS:
     if own in ROCK:
        return WIN
     if own in PAPER:
        return LOSE
     if own in SCISSORS:
        return DRAW

def asses_choice(choice: str) -> 'int':
   
   if choice not in ["X", "Y", "Z"]:
      raise ValueError(f"Invalid move - {choice}")
      return 0
   
   if choice == "X":
      return 1
   
   if choice == "Y":
      return 2
   
   if choice == "Z":
      return 3
   

def get_data(file_name: str) -> str:
   
  result: str

  with open(file_name, "r") as file:
    result = file.read()

  return result


def find_score(opponents_choice: str, score: str) -> str:
   
  ROCK = 'A'
  PAPER = 'B'
  SCISSORS = 'C'

  OWN = {
  ROCK: 'X',
  PAPER: 'Y',
  SCISSORS: 'Z'
  }

  WIN = 'Z'
  LOSE = 'X'
  DRAW =  'Y'

  if opponents_choice == ROCK:
      if score == WIN:
        return OWN[PAPER]
      if score == DRAW:
        return OWN[ROCK]
      if score == LOSE:
        return OWN[SCISSORS]
      
  if opponents_choice == PAPER:
      if score == WIN:
        return OWN[SCISSORS]
      if score == DRAW:
        return OWN[PAPER]
      if score == LOSE:
        return OWN[ROCK]
      
  if opponents_choice == SCISSORS:
      if score == WIN:
        return OWN[ROCK]
      if score == DRAW:
        return OWN[SCISSORS]
      if score == LOSE:
        return OWN[PAPER]