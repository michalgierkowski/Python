
# number list
num_list = [3,10,11,25,52]


# Easy - Section

# printing first and last number
# print(num_list[0], num_list[-1])
# 0 always first number, -1 always the last number

# Add a new number to end of the list, then print list
# num_list.append(74)  
# print(num_list)

# Remove the 3rd elemenht from the list, then print list
# num_list.pop(2)
# print(num_list)
# .pop() removes element by its position (index)
# .remove() removes element by its value 

# Loop through list and print each element on its own line
# for num in num_list:
    # print(num)


# Medium - Section


# Find largest number in list manually (no max())
# current_largest_number = num_list[0] First element of num list - stored as "current_largest_number" because we don't know largest number

# for num in num_list:                                  iterates num_list one by one
    # if num > current_largest_number:                  if this condition is true
        # current_largest_number = num                  replace the current "largest number" as the iterated num
#                                                       repeat this process till condition is false                                                          
#print(current_largest_number)                          print the largest number


  

# Find smallest number in list manually
# smallest_number = num_list[-1]                        starts with smallest element

# for num in num_list:                                  for each number in num_list     
    # if num < smallest_number:                         if iterated number is smaller than variable value
        # smallest_number = num                         set the variable as the current iterated value

# print(smallest_number)                                print once the loop has finished
        


# Calculate the sum and the average of all numbers in list manually (no sum() )
# total = 0                                             use "total" instead of "sum" as sum replaces sum() function
# average = 0                                           set both as 0

# for num in num_list:                                  for every number iterated
    # average += 1                                      add 1 to average variable (counts how many numbers there are)
    # total += num                                      add total to the current iterated value

# average = total / average                             once loop is finished, work out average
# print(f"Sum of list: {total}, Average of list: {average}")    print out final results




# Count how many numbers in the list are greater than 10
# total = 0                                             start with 0, we don't know how many numbers greater than 10

# for num in num_list:                                  for each number in list
    # if num > 10:                                      if current number is greater than 10
        # total += 1                                    add one to total
#                                                       else do nothing
# print(f"There are {total} numbers greater than 10")   show result
   



# Hard - Section


# Ask the user for a number. Search for it in the list manually.

#index = -1                                                 To start at 0                                             
#found = False                                              To track if number was found / matched
#user_number = int(input("Search for a number:  ").strip()) Ask user for input

#for num in num_list:                                       For each number
    #index += 1                                             Add 1 to index count / position
    
    #if num == user_number:                                 If iterated number matches with users number
        #found = True                                       Set "found" as True
        #if found == True:                                  if found is True              
            #print(f"Found at index: {index}")              print the output along with index  
#                                                           else
#if not found:                                              If found never was set to True
    #print("Not Found")                                     print the output

    
  
# Print only the even numbers from the list

# even_number = []                              empty list to store even numbers

#for num in num_list:                           for each number in list
    #if num % 2 == 0:                           if number divides evenly by 2
        #even_number.append(num)                add it to the even list
#                                               else do nothing

#print(f"Even numbers are --> {even_number} ")  show the even list



# Reverse the list manually

#reversed_list = []                             To store reversed list

#for i in range(len(num_list) - 1, -1, -1):     start, stop, step (where to start, where to stop just before (excludes), how many steps)
    #reversed_list.append(num_list[i])          uses index i to grab the value at the position in num_list
#print(reversed_list)   
        


   
# Create a new list that only contains numbers that area divisible by 3


# ivisible_by_3 = []                            Make a list for numbers divisible by 3 to be stored


# for num in num_list:                          
    #if num % 3 == 0:                           if each iterated number is divisble by 3 
        #divisible_by_3.append(num)             add it to the list

#print(divisible_by_3)