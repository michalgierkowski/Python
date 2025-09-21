# Loops

**Source:** HackerRank – Loops

**Goal:**  
Read an integer `n`. Print the square of each non-negative integer less than `n`.

**Attempt 1**
Follow "Attempt 1" in solution.py

First attempt:
- Hard-coded list [0,1,2,3,4] this meant that it would only when n = 5
- Any other input than 5 = fails
- if i < n --> is unnecesary 

**Attempt 2**
Follow "Attempt 2" in solution.py

Second attempt:
- Instead of hard-coding a list, used range of (0, n) which n being the integer entered 
- For example if n = 9 was entered the range would insist of (0 - 9) which goes up to n but not including n
- if i is smaller than X print i to the power of 2

