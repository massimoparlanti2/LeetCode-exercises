# LeetCode Python Solutions

This repository contains my solutions to **LeetCode problems** implemented in Python.  
Each solution is organized by difficulty and includes explanations, example test cases, and complexity analysis.  

## 📂 Repository Structure

leetcode-python-solutions/
│
├─ README.md # This file
├─ Python/
│ ├─ Easy/ # Easy problems
│ ├─ Medium/ # Medium problems
│ └─ Hard/ # Hard problems
└─ Notes/ # Algorithm notes, patterns, and explanations

- **Python/Easy, Python/Medium, Python/Hard**: Solutions organized by difficulty.  
- **Notes/**: Markdown files explaining patterns and algorithms (Dynamic Programming, Graphs, etc.).

---

## 📝 Problem File Template

Each Python file follows a consistent format:

```python
# Problem <ID> - <Problem Name> (<Difficulty>)
# URL: <LeetCode link>
# Description: Short description of the problem
# Example:
#   Input: ...
#   Output: ...

from typing import List

def function_name(params: Type) -> ReturnType:
    """
    Brief explanation of the approach
    """
    # Implementation here
    pass

# -----------------------------
# Example / Test
# -----------------------------
if __name__ == "__main__":
    test_cases = [
        (input1, input2, expected_output),
        ...
    ]
    for inputs in test_cases:
        result = function_name(*inputs[:-1])
        print(result)
        assert result == inputs[-1]
Includes type hints, example test cases, and assert checks.
Each solution mentions Time and Space Complexity for clarity.