# Leap Year

**Source:** [HackerRank – Write a Function] - (https://www.hackerrank.com/challenges/write-a-function/problem)

**Goal:**  
Determine if a given year is a leap year using Gregorian calendar rules.



## Key Rules
- Divisible by 400 -> leap year   
- Else if divisible by 100 -> not a leap year   
- Else if divisible by 4 -> leap year   
- Else -> not a leap year   



## What I Learned
- The **order of conditions matters**.  
- If % 4 is checked before`% 100, years like 2100 are wrongly counted as leap years.  
- Constraints help know which cases to test (e.g., 1900, 2000, 2100).  
- Writing conditions step by step makes the logic easier to debug.