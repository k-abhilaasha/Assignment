#accept input from user
x=int(input("enter a number"))
#if x is a negative number it prints false
if(x<0):
    print("False")
#x is positive checks the below condition
else:
    rev=0
    temp=x
    while x>0:
        #modulo oprator gives remainder
        rem=x%10
        rev=(rev*10)+rem
        #// is the floor operator which gives rounded value
        x=x//10
#if given input is equal to reverse of the input it gives true or it gives false
if(temp==rev):
    print("True")
else:
    print("False")


