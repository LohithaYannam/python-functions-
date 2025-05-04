#write a program to return multiple values
#min,max,avg by passing 1,2,3,4,5 to a function
def values(numbers):
    return min(numbers),max(numbers),sum(numbers)/len(numbers)
max_value,max_value,avg=values([1,2,3,4,6,5])
print(f"min:{min_value},max:{max_value},average:{avg}")
