# Beginner Level


# First Character
# [start: end : step]

text = "Python"
# Get the first character

print(text[0])

# result = ✅ Correct!

# 2. Get the last character of this string:

word = "Programming"

print(word[-1])  # negative indexing

# result = ✅ Correct!

# 3. Get the middle character (assume the string length is odd):

name = "Giraffe"

print(name[3])

# result = ✅ Correct!

# Problem 4 (Indexing only)

phrase = "ABCDEFGHIJ"
# Print characters at index 0, 2, 4, 6, 8

print(phrase[::2])

# result = ✅ Correct

# Extract "world" from the string using slicing:

message = "Hello, world!"
# Use slicing to print just "world"

print(message[-6:-1])

# result = ✅ Correct

# Problem 7

fruit = "banana"
# Replace the first character with "c" to make "canana"

print(fruit.replace("b","c"))

# result = ✅ Correct but not "string indexing"

print("c" + fruit[1:])  # excludes the letter "b" at index 0 and replaces with "c"
# fruit[0:] would ADD "c" to banana --> cbanana instead of replacing b
# Correct way with indexing

# Problem 8
# Swap the first and last characters of this string using slicing and indexing only:

s = "coding"
# Expected result: "godinc"

print("g" + s[1:-1] + "c")

# works but is only hardcode to "g" and "c"
# correct way below

print(s[-1] + s[1:-1] + s[0])  # print -1 which is "g" + [1:-1] which is o -> n (this is because -1 is already used before) + [0] which is "c"

# Challenge 9:

phrase = "OpenAI is amazing"

# Use string slicing and indexing to print this exact output:
# A I

print(phrase[4] + " " + phrase[5])

# CORRECT POGGERS

# 🔥 Challenge 10:
# Given the string:
text = "DataScience"
# Print this exact output using slicing and indexing only:
# Scece

print(text[4:6] + text[7] + text[9:11]) # grabs characters position of 4 and 6 (6 because stop is excluded meaning stops before)
# + [7] is the singular text and [9:11] are "ce" same as above 11 because it stops before the stop


# Correct


#  last question

s = "backflip"
# make it print "flip"

print(s[4:])

