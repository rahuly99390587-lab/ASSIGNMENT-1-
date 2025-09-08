import math


#ask user for input
num=float(input("enter your number:"))
print("\nResults:")

#Square root

if num>=0:
    print("Square root:",math.sqrt(num))
else:
    print("Square root:not defined for negative number")  

    #Natural log (ln) 

if num>0:
    print("Natural logarithm",math.log(num))
else:
    print("Natural logarithm:not defined for zero or negative numbers") 


# sine (in radians)  
print("sine",math.sin(num)) 

#cos (in radians)
print("cos",math.cos(num))

# tan (in radians)
print("tan",math.tan(num))



