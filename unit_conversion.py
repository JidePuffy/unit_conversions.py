import math

#  To convert Fahrenheit to degrees Celsius = "amount and then multiply it by the fraction 5/9." 


# fahrenheit = float(input("What is the temperature in fahrenheit?"))
# celsuis = (fahrenheit - 32) * (5/9)
# print(f"The temperature in Degree Celcius is {celsuis:.1f}")

#QUESTION 2

# Determine how fast an object will fall.

# THE PHYSICS
# If you release an object (ball, rock, whatever) from rest (or you could throw it) and let it fall through a fluid, the change
# in speed of the object is affected by several things: the mass of the object, the acceleration due to gravity, the shape of 
# the projectile, the size of the projectile, and the density of the fluid.

# The function that computes the speed after "t" seconds have elapsed is given by:

# v(t) = sqrt (mg/c) * (1 - exp((-sqrt (mgc) / m) t ))

# Hint from Instructor:
# Please note that this formula is written the way you would see it in a Physics textbook and cannot directly be copied
#  and pasted into Python code. For example, "mg" really means "m * g".

# Also, the expression "v(t)" is how the physicist is communicating "velocity at time t", in your python code,
#  you wouldn't want to put parentheses, but instead could just name a variable velocity or velocity_at_t or something similar.

# The expression: "exp(xxxx)" means the Mathematical number "e" to the power of xxxx. In Python, you can calculate this using 
# the library function math.exp(xxxx).

# The expression: "sqrt(xxxx)" means the square root of xxxx. You can calculate the square root in Python using math.sqrt(xxxx)

# Where:

# m = mass (in kg)

# g = acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)

# t = time (in seconds)

# c = 1/2 p A C

# p = density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)

# A = cross sectional area of projectile (in square meters)

# C = drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)

# exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).

# sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).


#SOLUTION
# import math

# m = 5
# g = 9.8
# t = 10
# p = 1.3
# A = 0.01
# C = 0.5
# exp = 2.71828

# #To get c
# c = (1/2) * p * A * C

# #To get mg
# mg = m * g
# mgc = m * g * c

#To get e
#e = float (math.exp(exp))

# velocity_at_t = float (mg /c) * (1 - math.exp (( - math.sqrt(mgc) / m) * t))
# print(float(velocity_at_t))
# solve = 1 - exp
# print(float(solve))

# COMPARING NUMBERS

# Write a program that asks the user for two integers.

# Then, write three separate if/else statements as follows:

# If the first number is greater than the second, print "The first number is greater". Otherwise, print 
# "The first number is not greater".

# If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

# If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

first_num = 7
second_num = 8

if first_num > second_num:
    print("First number is greater")
else:
    print("The first number is not greater")

if first_num == second_num:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_num > first_num:
    print("The second number is greater")
else:
    print("The second number is not greater")

fav_animal = input("What is your favorite animal?")

if fav_animal.lower() == "dog":
    print("That's my favorite animal too")
else:
    print(f"{fav_animal} is not my favorite animal.")



