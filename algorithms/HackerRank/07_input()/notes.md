# input() - polynomial

**Source:** [HackerRank – Input()](https://www.hackerrank.com/challenges/input/problem?isFullScreen=true)


**Goal:**  
- Given with polynomial P and values of x and k.
- Task is to verify if P(x) = k


## My First Attempt
- **x**, **k**, took two integers and assign them to separately
- **split()**, to grab string values and returns into a list
- **map()**, to apply a given function to every item in a iterable -> map(function, iterable)
- **int()** (the function called), was applied to each string within the list
- **P (polynomial)** as formula: (x**3) + (x**2) + (x) + 1
- When Python sees a variable in an expression, it replaces the variable name with the value stored in it and then does the calculation
- Compared whether **P** is equal to **k**
- If **P** was equal to **k**, print **True**
- Else print **False**


## Final Version
- Repeated line 1 for attempt 1
- Previous mistake was formula for **polynomial** was hard-coded
- **expr** as input() -> allows any formula to be entered
- Compared if value of the expression (the **eval()** function) of **expr** was equal to **k**
- If it was equal to **k**, print **True**
- Else print **False**


## What I Learned
- **split()** (method), allows to grab string values and return it as a list
- **map()** (function), to apply a given function to all elements in a iterable 
- **eval()** (function), takes string as input and runs it as code, if valid it will be excuted otherwise a error will occur
- Need to take time with reading questions, instead of skimming and replicating the example.


## Quick Example
Input:  1 4
Output:  True