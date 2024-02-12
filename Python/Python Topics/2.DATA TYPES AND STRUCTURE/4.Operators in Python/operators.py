# operators in python

#symbols

# 1) Arithmatics operators  : used for mathematical calculation

# +:Addition
# -:Subtraction
# *:Multiplication
# /:Division 
# % - modulus
# ** - exponentiation
# // - floor division

# #examples :-

# x = 6 
# y = 4
# print(x+y) #10
# print(x-y) #2
# print(x*y) #24
# print(x/y) #2.5
# print(x%y) #2
# print(x**y)#1269
# print(x//y)#1

# 2) Assighment operatos:-Assighn values to operators
# = (Equal to)
# +=,-=,*= : Argument assignment

# example
# x = 10
# x -=5
# print(x)#5
# x = 20
# x *= 2
# print(x)#40

# 3) Comparision Operators:-compare values and return boolean(T/F)
# == equal to
# != not equal to 
# < less than
# > greator than
# <= less than or equal to 
# >= greator than or equal to

# x = 10
# y = 15
# print(x==y)#F
# print(x!=y)#T
# print(x<y)#T
# print(x>y)#F
# print(x<=y)#T
# print(x>=y)#F/

# Logical operator : combimn boolean values:
# and : true if both opeands are true
# or : true if only one operands is true
# not : inverted the operands truth value

# x = 10 
# y = 15
#     F         T  false
# print(x>y and x<y) #false
#     F       T   true
# print(x>y or x<y) #true
# print(not x>y) #true

# 5) Identity operators:- check object identity:
# is 
# is not 
# x =10
# y =15
# print(x is y) # F
# print(x is x) # T
# print(x is not y) #T

# 6) membership operators  :- check if values is in a sequence:

# print("x" in "xmas") #T
# print("x" in "z") # F
# print("x" not in "z") # T

# 7) Bitwise operators:- perform operation on the binary representation of numbers:
# &:Bitwise AND
# |:Bitwise OR
# <<:Left shift
# >>:Right shift
# examples
# print(5&3)
# print(5|3)
# 5<<2 #20
# 5>>1 #2

#Swapping values:
# x = 5
# y = 4
#your code
#1) using = operators
# x,y=y,x

#2) using a third variable 
# z = x # 5
# x = y # 4
# y = z # 5
# print(x) #4

#3) using calculation
# x = x+y #9
# y = x-y #5
# x = x-y #4
# print(x) # 4
# print(y) #5
