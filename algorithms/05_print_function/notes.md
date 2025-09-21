# Problem Title

**Source:** [Hackerrank – Print Function](https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true)

**Goal:**  
Without using any string methods, try to print the following:
123....n, "...." represents the consecutive values in between.


## My First Attempt
- Used a list to store numbers that add up to n
- Used variable "i" with value of 0 
- Used a while loop due to not knowing what the input will be
- Two conditions
- First to check if "i" is not equal to n -> if not to add 1 to "i" then append into list -> repeat
- Second to check if "i" is equal to n -> end the loop
- Final step was to use a for loop to iterate through the list
- Change int -> str and print them next to each other (with "end=")

## Final Version
- Use for loop in a range of (1 to n + 1), meaning all numbers between 1 and n + 1 would be counted
- This allows for "n" to be counted aswell as in a range the "stop" would be excluded, in this case the value of "n"
- Use "end=" once again to print on same line, but did conversion of int -> str within the print, instead of before-hand

## What I Learned
- To review code once written and look for a "sharper" possibility
- "end=" places all values on the same line
- Mini-tricks such as doing calcuation in the range (1, n + 1) is easier than managing a list

## Quick Example
Input: 5
Output: 12345