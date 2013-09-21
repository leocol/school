'''
Author: Leo Collins
CS 201, Sept. 16, 2013
Simple Interest

Algorithm:
1. Ask user for principal
2. Ask user for number of years
3. Ask user for rate of interest
4. Multiply these three figures together
5. Take this result and divide by 100
6. Print simple interest

Test Case:
1. Principal - 10000. Years - 5. Interest rate - 12.5
Expected outcome - 6250.
2. Principal - 15000. Years - 20. Interest rate - 6
Expected outcome - 18000.

Result: Works as expected
'''
principal = int(input("Please enter your principal: "))
years = int(input("Please enter the number of years: "))
interest = int(input("Please enter your rate of interst: "))
undivided_interest = principal * years * interest
simple_interest = undivided_interest / 100
print ("Your simple interest is", simple_interest)


