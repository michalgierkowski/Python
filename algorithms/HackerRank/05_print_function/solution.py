# My First Attempt
if __name__ == '__main__':
    n = int(input())
    numbers = []
    i = 0
    
    while True:
        if i != n:
            i += 1
            numbers.append(i)
        elif i == n:
            break
    
    for num in numbers:
        num = str(num)
        print(end=num)

# Final Version
if __name__ == '__main__':
    n = int(input())
    
    for i in range(1, n + 1):
        print(end=str(i))