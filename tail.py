#tail
def ftail(n,acc=1):
    if n==0 or n==1:
        return acc
    return ftail(n-1,n*acc)
print(ftail(5))
 
