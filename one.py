""" name ="Mickey"
age =19
location="Kavre"

#concate method
print("My name is " + name + "my age is" + str(age) + "address is" + location)

#fstring method(widely used)
print (f"My name is {name} and my age is {age} and address is {location}")

#format old version method
print("my name is %s and age is %d and address is %s " %(name,age,location))

#format new version method
print("My name is {0} and age is {1}" . format(name,age))

print(type(name, location))       #indicates the datatype of the variable, here it shows str as name is string


print(type(age))        #returns int as age is integer




# This is single-line comment ctr+/

This is multiple line comment, shift+alt+A """

#Finding sum and datatype of sum
""" num1=(input("enter the first number\n"))
num2=(input("enter the second number\n"))
num3=int(input("enter the third number\n"))
num4=int(input("enter the fourth number\n"))

sum1= num1+num2
type1= type(sum1)
print(f"The first sum is {sum1} and its datatype is {type1}")


sum2= num3+num4
type2= type(sum2)
print(f"The second sum is {sum2} and its datatype is {type2}")

 """


#true and false value
#if and is used then it returns first value, if bothh true then last value
#if or is used then it return first true if both false then last value

# print(6 and 7)  #returns last value which is 7

# print(0 and "") #returns 
# print(1 or 7)
# print(0 or 6)

# print(0 or "")


# print('apple' < 'Apple') this related ASCII value to return true or false, q-z= 97-122 and A-Z= 65-90

#ordinals
# print(ord('A'))
# print(ord('😔'))


# #character
# print(chr(67))

#Escape sequence
""" print("My name is \t") #
print("My name is \n") #takes to new line
print("My name \ris ") #replaces whatever is after the r """

#Operators(VVIP)
            # $they are symbol or keyboard used in calculation
#    Operands are the values used to perform calculations, they are; unary amd binary.         

# Floor division

# print(-5//2)

# Compound Assignment += or -= , better aproach

# Logical Operators and or not.
            # 1/0 is division error it is logicla error print (false or 1/0)
#Bitwise operators, print(5 & 4) print(5  4), 

# print(5 & 9 )  
# 7<<2(7*2 power 2)   7>>2(7/(2 power 2)) #not print()

#membership and identity
""" 
a=[1,2,3]
b=[1,2,3]
c=a
print(a is b)   #returns false as their memory is different
print(a == b)  #returns true as the operator checks only the value
print(a is c)    # returns true because c=a makes their memory as same
print(id(a))    #returns the memory allocation id for the variable a
print(id(b))     #returns the memory allocation id for the variable b
print(id(c))    #returns the memory allocation id for the variable c. which is same as id of a """


