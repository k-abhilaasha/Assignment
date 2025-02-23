def isPalindrome(x):
        # Edge case: negative numbers are not palindromes
        if x < 0:
            return False
        temp= x
        #here rev is reverse of the number
        rev= 0
        
        while x > 0:
            #modulo operator gives the remainde
            rem = x % 10
            rev= (rev * 10) + rem
            #// floor operator give rounded number
            x //= 10
        
        return temp==rev
x=int(input("enter a number:"))
result=isPalindrome(x)
print(result)