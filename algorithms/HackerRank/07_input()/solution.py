# My First Attempt
x, k = map(int, input().split())
P = x**3 + x**2 + x + 1

if P == k:
    print("True")
else:
    print("False")

# Final Version
x, k = map(int, input().split())
expr = input()

if (eval(expr)) == k:
    print("True")
else:
    print("False")