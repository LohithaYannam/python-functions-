#direct recursion
def fact(n):
    if n == 0 or n == 1:  # Base case to stop recursion
        return 1
    return n*fact(n-1)
print(fact(5))
