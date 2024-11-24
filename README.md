# LeetCode Practice Repository

Welcome to my **LeetCode** repository! This repository is a collection of coding exercises I've worked on to improve my problem-solving skills and deepen my understanding of various algorithms and data structures.

## 📚 Contents

The repository is organized into multiple sections based on problem difficulty and purpose:

1. **Easy**
2. **Medium**
3. **Hard**
4. **Helper Scripts**: Utility scripts to assist in problem-solving and file management.

## 🚀 Key Features

### Daily Problem Template Creation
This repository includes a handy script, `create_daily_problem_file.py`, designed to streamline the process of setting up files for new problems. It helps create a Python template for solving problems with a consistent naming convention.

#### How It Works:
When you run `create_daily_problem_file.py`, it prompts you to:
1. Enter the problem name and its associated ID.
2. Specify the difficulty level (1: easy, 2: medium, 3: hard).

Example interaction:
```
Enter the name of the problem: 1975. Maximum Matrix Sum
Enter the difficulty level (1: easy, 2: medium, 3: hard): 2
File created: ../medium/maximum_matrix_sum_1975.py
```

The script automatically generates a new Python file in the appropriate directory (`easy/`, `medium/`, or `hard/`) with the correct filename format. This saves time and keeps the repository organized.

### Testing Suite - 😋 Work in Progress 😋
The `tests/` folder includes unit tests for selected problems to ensure solutions are correct and maintainable. For example, `test_27_remove_element.py` contains tests for the "Remove Element" problem.


### File Structure

```
leetcode/
├── easy/
├── medium/
│   ├── __init__.py
│   ├── XXXX_README.md
│   └── <medium_exercise_name>_XXXX.py
├── helper/
│   ├── __init__.py
│   ├── create_daily_problem_file.py
│   └── tester.py
├── tests/
│   ├── easy/
│   │   ├── __init__.py
│   │   └── test_27_remove_element.py
│   └── __init__.py
└── README.md
```

## 🛠️ How to Use

1. **Creating a Problem File**  
   Run `create_daily_problem_file.py` from the `helper` directory and follow the prompts to set up a new problem file.

2. **Solving Problems**  
   Navigate to the respective directory (`easy`, `medium`, `hard`) and add your solution to the created template.

3. **Testing Solutions**  
   (Ideally) Use the test scripts in the `tests/` directory to verify your solutions.

4. **Viewing Progress**  
   The repository is structured for easy navigation and review of solved problems.

## 🌟 Contributions

This repository is a personal practice space, but feel free to suggest improvements or alternative approaches to the solutions.

## 🧑‍💻 About Me

I’m passionate about problem-solving and continually honing my coding skills. LeetCode has been a go-to platform to learn, practice, and explore new algorithms and concepts.

## 🚀 About Me
I'm a full stack developer...

