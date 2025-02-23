#import math library which contains all the mathematical operations
import math
#def a function to calculate lcm and gcd
def lcmAndGcd(a,b):
    #as math contains all the operations it will directly calculates the gcd and lcm
    gcd=math.gcd(a,b)
    lcm=math.lcm(a,b)
    return [lcm,gcd]
#access input from users
a=int(input("enter first number:"))
b=int(input("enter second number:"))
#call the fuction and display the result
result=lcmAndGcd(a,b)
print(result)
        