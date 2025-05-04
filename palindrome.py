#create a program to determine if a string is a palindrome by recursively comparing characters from start to end by base case function and call if the pointer meets its palindrome constraints:
#def is_palindrome length
#def check palindrome start,end,s
#input:
#racecar=True
#hello=False
#level=True
def is_palindrome(s):
    if len(s)<=1:
        return True
    return check_palindrome(s,0,len(s)-1)
def check_palindrome(s,start,end):
    if start>=end:
        return True
    if s[start]!=s[end]:
        return False
    return is_palindrome(s[start+1:end])
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("level"))
