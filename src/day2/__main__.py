import app1
import app2

import os

if __name__ == "__main__":
  
  print("Solution for task1:")
  print(app1.main(os.path.join(os.path.dirname(__file__), "./input1.txt")))
  print("Solution for task2:")
  print(app2.main(os.path.join(os.path.dirname(__file__), "./input1.txt")))