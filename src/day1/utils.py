def get_data(filename: str) -> str:
  result: str

  with open(filename, "r") as file:
    result = file.read()

  return result

def parse_list(raw_list: str) -> list[list[int]]:

  list_of_strings = raw_list.strip().split("\n\n")
  list_of_lists = [[int(sub_list) for sub_list in string.split('\n')] for string in list_of_strings]

  return list_of_lists