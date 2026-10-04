#Operators in Python: special keywords that tells python to perform a special computation. 
        # 7 types of operators
    
# 1. Arithmetic Operators( + ,- ,*, /, //, %, ** )

#Normal Arithmetic operation
print(8+5) #13
print(8-5) #3
print(8*5) #40

#Normal Division
print(9/2) #print 4.5 '/' always returns float
print(64/8) #print '8.0' not '8'

#Floor division
print(9//2) #prints 4, returns integer value rounded off to nearest whole number
print(-9//2) #prints -5, goes to nearest whole number, which is -5(or goes near zero)

#Modulus(used to check odd and even in programming)
print(4%2) #0, returns the remainder 
print (29%5) #4, returns the remainder

#Exponent
print(2**4) #16, as it means 2 to the power 4
print(81**0.2) #9.0 (square root)
print(512**1/3) #8.0 (cube root)


# 2.Comparison (Relational Operators)
    # (==, !=,>,<, <=,>=)

    #Compare
print(8==8) #true, it compares 8 with 8 with is true
print(9!=10) #true, it compare 9 with 10, which is not true, so returns true
print(5<9) #true, compares 5 and 9 and gives result
print(10>5) #true, compares 10 and 5 and returns result

a=15
print(1<a<20) #true checks if a=15 lies in between 1.00001... and 19.999 and returns the result
print(1<=a<=20) #true checks if a=15 lies between 1 and 20 or not
print(5>a>20) #false checks if 5>a and a>20 both
print(20>=15>=30) #false, checks 20>=15 and 15>=30, which is false

#String Comparison(unicode/ASCII value comparison)
print("guava" > "banana") #true, 'g' >'b' in unicode[A-Z(65-90)    a-z(97-122)]
print("Guava" < "guava") #true, 'G' has greater value than 'b' so it is true
print("Ram"=="ram"), #false, this is case-sensitive one R is not equal with r

print(9 == "9") #false, as 9 is int and "9" is a str



# 3. Assignment Operators(=, +=, -=, *=, /=, //=, %=, **=)

#Compound Assignment
age=10
age+=5 #age is now 10=15
age-=5 # age is now 15-5=10
age*=2 #age=age*2, age is now 10*2=20
age/=5 #age=age/5, 20/5= 4.0
print(age) #returns 4.0

# Multiple value assign

#print the same assigned value
x=y=z=1 #x,y,z all becomes 1
print(x,y,z) #1 1 1

#assign different values
x,y,z = 1,2,3
print(x,y,z) #1 2 3

#swap variables
x,y=5,8
y,x=5,8 #swaps the values into variables
print(x,y) #prints 8 5

# 3. Logical Operators[and(&&) or(||)], python uses words 'and', 'or' and 'not' rather than symbols
        #trick: know the formulas for the 'and' 'or' 'not' gates + truthy and falsy value concept

        # 'and' Returns the first falsy value it finds.If all values are truthy, returns the last value.
        # 'or' Returns the first truthy value it finds.If all values are falsy, returns the last value.

 # Combining logical operators and comparison operators
std_mark=50
print(std_mark>=30 and std_mark<=100 )  
           #true        #true       #returns true, compares the two values

print(std_mark<40 or std_mark<100)
        #false          #true    #eturns true, or operator

#examples of and, or not operators
is_tall=True
is_short=False
print(is_tall and is_short) # returns false
print(is_tall or is_short) #returns true
print(not is_tall) #returns false as it inverts the result

#examples of Short-circuit with and
print(False and 1/0) # False (no ZeroDivisionError!)
print(True and 1/0) #zeroDivisionerror

#examples of Short-circuit with or
print(True or 1/0) #true (no zeroDivisionError)
print(False or 1/0) #zeroDivisionerror


# 4. Bitwise operator(0 and 1 operations)
bin(5) #converts 5 into binary string notation,'0b101'
int('0101', 2) #converts a binary string back to decimal number.

#And bitwise operator
print(5 & 2)#compares the binary values and returns 0

#   0 1 0 1(5)
# & 0 0 1 0  (2)
# -----------
#   0 0 0 0  (Binary for 0)

#Or bitwise operator
print(5 | 2) #returns 7

#   0 1 0 1(5)
# | 0 0 1 0  (2)
# -----------
#   0 1 1 1  (Binary for 7)

#XOR bitwise operator
print(5^2) #returns 7, returns true value when both input are different.

#   0 1 0 1  (5)
# ^ 0 0 1 0  (2)
# -----------
#   0 1 1 1  (Binary for 7)

#Left shift- mulitply by powers of 2
print(5 <<1) # return (5*2=10)
print(5 << 2) # return (5*2*2=20)

#Right shift- divide by powers of 2
print(8>> 1) # return (8/2=4)
print(8 >>2) # return (8/4=2)


# 5. Membership and Identity Operators

# Membership Operators('in'and'not in')
print("Ram" in "Ramayan") #True, checks the sequence of characters rather than ASCII value
print("Python" in "python")#false, case-sensitive
print("s" not in "Mickey") # true, bcz s is not in Mickey

 #Identity Operators(is, 'is not')
a= [1,2,3]
b=[1,2,3]
c=a
print(a==b) #true(== checks the equality of values)
print (a is b) #False (different objects in memeory)
print(a is c) #true,(same object, as c=a)

#Note: Warning******
print(2*3*2) #2 ko power ma 3, 3 ko power ma 2,( 2^3)^2

print(~9) # -(x+1), -(9+1)= -10
print (~(-9)) # -(x+1), -(-9+1)=8











