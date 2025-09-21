# Attempt 1
if __name__ == '__main__':
    n = int(input())
    
    numbers = [0,1,2,3,4]
    
    for num in numbers:
        num_result = num ** 2
        print(num_result)



# Attempt 2
if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        if i < n:
            print(i ** 2)
    