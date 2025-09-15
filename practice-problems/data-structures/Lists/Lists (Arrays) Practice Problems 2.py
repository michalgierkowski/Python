# Day 2 revisit

#num_list = [2,15,6,51,33]


# Easy

# print the list length without using len()

#length = 0                                   Start at 0     
#for num in num_list:                         for every loop through element
    #length += 1                              add one to length

#print(f"The length of the list is: {length}")


# Add 2 numbers at the end of the list, then print updated list

#num_list.extend([3, 6])                      .extend loops through iterable (list []) and adds each element to the list - good for multiple of elements
#num_list.append(3)                           .append adds a single element - good for adding one element

#for num in num_list:
    #print(num)


# Remove the first element from the list (two different types of ways), then print updated list

#num_list.remove(2)                            removes by value (the first occurrence of value )
#num_list.pop(0)                               removes by index (the index added)

#for num in num_list:
    #print(num)



# Loop through the list and print each element, but this time print the index and the value.

#index = -1                                    set variable at -1, stored outside of loop so doesn't reset every loop               

#for num in num_list:                                            
    #index += 1                                each iteration adds 1 to index 
    #print(f"{index} - {num}")                 index matches the position of num in list


# Medium


# Find the second largest number in the list manually

# we start from index 0, not a certain element
#largest_number = num_list[0]                           
#second_largest_number = num_list[0]


#for num in num_list:
    #if num > largest_number:                                       if num is bigger than largest number
        #second_largest_number = largest_number                     set the second largest as the previous value for largest number
        #largest_number = num                                       set the new largest number as current num
    #elif num > second_largest_number and num != largest_number:    if number is greater than second largest number and number is not equal to largest number
        #second_largest_number = num                                set a new value for second largest number
#print(f"The second largest number is {second_largest_number}")




# Struggled with previous same question styles

# Find the second smallest number in list manually

# Where numbers get stored
#smallest = num_list[-1]                                start at index 0 of list  
#second_smallest = num_list[-1]

#for num in num_list:
    #if num < smallest:
        #second_smallest = smallest                     store the old "smallest" as "second smallest"
        #smallest = num                                 then update "smallest" 
    #elif num > smallest and num < second_smallest:     if number is bigger than smallest and less than second smallest
        #second_smallest = num                          store it as second smallest

#print(f"Smallest: {smallest}")
#print(f"Second smallest: {second_smallest}")




# Find the third largest number

#"-inf" - smaller than anything 
#largest = float("-inf")                
#second_largest = float("-inf")
#third_largest = float("-inf")


#for num in num_list:
    #if num > largest:                                      works like a podium
        #third_largest = second_largest                     third becomes previous second largest
        #second_largest = largest                           second becomes previous largest
        #largest = num                                      largest becomes current number

    #elif num > second_largest and num != largest:          else if number is greater than second and is not equal to largest
        #third_largest = second_largest                     third becomes previous second largest
        #second_largest = num                               second largest becomes current number

    #elif num > third_largest and num != second_largest and num != largest:   else if number greater than third and not equal to second,largest
        #third_largest = num                                                  set third as current number

#print(largest)
#print(second_largest)
#print(third_largest)



# Write a program to find how many unique pairs of numbers in a list add up to 10
# No pairs edition

#add_up_to_10 = []                                      Empty list to collect pairs that add up to 10

#for i in range(len(num_list)):                         Picks first element by it's position (index)
    #for j in range(i + 1, len(num_list)):              Picks second element by it's position but not allowing any duplicates
        #if num_list[i] + num_list[j] == 10:            if the index(i) element + index(j) element == 10               
            #add_up_to_10.append((num_list[i], num_list[j]))    if yes, store this as tuple
#                                                               after loop
#if len(add_up_to_10) == 0:                                     if list is empty
    #print("There are 0 pairs that add up to 10!")              output that there are no pairs
#else:
    #print(f"There are {len(add_up_to_10)} pairs that up to 10:")   else show how many pairs there are
    #for pairs in add_up_to_10:
        #print(pairs)                                               what the pairs are




# Write a program to find how many unique pairs of numbers in a list add up to 15
# Pairs edition


#num_list = [5, 10, 7, 8, 12, 3, 9, 6]                  list of pairs that add up to 15                 
#add_up_to_15 = []                                      Empty list for valid pairs

#for a in range(len(num_list)):                         outer loop - grabs the first number of the pair
    #for b in range(a + 1, len(num_list)):              inner loop - grabs the second number of the pair     
        #if num_list[a] + num_list[b] == 15:                    if index a value + index b value is equal to 15
            #add_up_to_15.append((num_list[a], num_list[b]))    store it as tuple and add it to the list

#if len(add_up_to_15) == 0:                                     if there are no pairs in list
    #print(f"There are 0 pairs that add up to 15.")
#else:
    #print(f"There are {len(add_up_to_15)} pairs that add up to 15:")   otherwise print how many pairs, and what they are
    #for pairs in add_up_to_15:
        #print(pairs)   