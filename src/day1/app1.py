import os
import utils

def main(filename: str) -> int:
  result: int

  data:str = utils.get_data(filename)
  calories_owned_by_elf = utils.parse_list(data)


  calorie_sum_by_elf:list[int] = [sum(elf) for elf in calories_owned_by_elf]

  result = max(calorie_sum_by_elf)

  return result
