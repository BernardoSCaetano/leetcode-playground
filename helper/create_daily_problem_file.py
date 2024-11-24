import os
from datetime import datetime

def create_daily_problem_file():
  # Get the name of the problem
  name = input("Enter the name of the problem: ")
  problem_number, problem_title = name.split(". ", 1)

  # Format the base file name
  base_file_name = problem_title.replace(" ", "_").lower() + "_" + problem_number
  file_name = f"{base_file_name}.py"

  # Get today's date
  date = datetime.today().strftime("%d-%m-%Y")

  # Select difficulty level from one of the options: 1 (easy), 2 (medium), 3 (hard)
  difficulty_map = {"1": "easy", "2": "medium", "3": "hard"}
  difficulty_choice = input("Enter the difficulty level (1: easy, 2: medium, 3: hard): ")
  difficulty = difficulty_map.get(difficulty_choice)
  if difficulty is None:
    print("Invalid difficulty level. Please enter '1', '2', or '3'.")
    return

  directory = os.path.join("..", difficulty)
  os.makedirs(directory, exist_ok=True)

  # Check if the file already exists and create a new version if necessary
  version = 0
  while os.path.exists(os.path.join(directory, file_name)):
    version += 1
    file_name = f"{base_file_name} ({version}).py"

  file_path = os.path.join(directory, file_name)

  # Create the Docstring for the file with the current date
  docstring = f'""" Problem: {name}\n Date: {date}\n"""'
  imports = f'\nfrom typing import List\n'  # Creating an empty class Solution
  class_solution = f'\n\nclass Solution:\n'  # Creating an empty class Solution

  # Write the content to the file
  with open(file_path, "w") as file:
    file.write(docstring)
    file.write(imports)
    file.write(class_solution)

  print(f"File created: {file_path}")

create_daily_problem_file()