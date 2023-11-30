import utils

def main(file_name: str) -> int:

  result:int = 0 
  raw_matches = utils.get_data(file_name)

  matches: list[str] = [match for match in raw_matches.strip().split("\n")]
  choices: list[list[str]] = [choice.split() for choice in matches] 

  for [opponent, score] in choices:
    own = utils.find_score(opponent, score)
    result = result + utils.evaluate_match(opponent, own) + utils.asses_choice(own)

  return result