'''
Author: Leo Collins
CS 201, Sept. 17, 2013
Lab 2, Question 2, Fahrenheit Conversion

Algorithm:
1. Ask user for degrees in fahrenheit.
2. Take the fahrenheit value and subtract 32
3. Take this value and multiply it by 5/9. This is the celsius value.
4. Take the celsius value and add 273.
5. This is the kelvin value.
6. Print the celsius and kelvin values.

Test Case:
1. Fahrenheit = 32.
Expected outcome: Celsius = 0. Kelvin = 273.
2. Fahrenheit = 75.
Expected outcome: Celsius = 23.89. Kelvin = 296.89.

Result: Works as expected
'''

fahrenheit = int(input("Please enter fahrenheit: "))
celsius = (fahrenheit - 32) * (5/9)
kelvin = celsius + 273
print ("This value of fahrenheit converted to celsius is", celsius)
print ("This value of fahrenheit converted to kelvin is", kelvin)
# I'm interested in how I may be able to have this program, in a sense,
# to loop back to the beginning so that the user may be able to continuously
# find conversions multiple times without having to restart the program altogether.

