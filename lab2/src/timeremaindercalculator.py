'''
Author: Leo Collins
CS 201, Sept. 17, 2013
Lab 2, Question 4, Time Remainder Calculator

Algorithm:
1. Ask user for an amount of seconds.
2. Divide this number by 3600. The whole number will be the amount of hours. 
3. Divide the remainder by 60. The whole number will be the amount of minutes.
4. The remainder will be the number of seconds. 
5. Print results

Test Cases:
1. Seconds: 7263
Expected outcome: 2 Hours, 1 Minute, 3 Seconds
2. Seconds: 5537
Expected outcome: 1 Hour, 32 Minutes, 17 Seconds

Result: Working as expected.
'''

total_seconds = int(input("Please enter the total amount of seconds: "))
hours_whole = int(total_seconds / 3600)
hours_remainder = total_seconds % 3600
minutes_whole = int(hours_remainder / 60)
minutes_remainder = hours_remainder % 60
seconds = minutes_remainder
print ("The amount of seconds you provided translates to", hours_whole, "hour(s),", minutes_whole, "minute(s), and", seconds, "second(s).")




