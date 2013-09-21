'''
Author: Leo Collins
CS 201, Sept. 17, 2013
Lab 2, Question 3, Seconds Calculator

Algorithm:
1. Ask user for number of hours, minutes, and seconds.
2. Take the number of hours and multiply by 3600.
3. Take the number of minutes and multiply by 60.
4. Add these two figures together, and then add on the seconds entered by user.
5. Print total number of seconds.

Test Cases:
1. Hours: 2. Minutes: 1. Seconds: 3.
Expected outcome: 7263 seconds
2. Hours: 1. Minutes: 32. Seconds, 17.
Expected outcome: 5537 seconds

Result: Working as expected.
'''

hours = int(input("Please enter the number of hours: "))
minutes = int(input("Please enter the number of minutes: "))
seconds = int(input("Please enter the number of seconds: "))
hour_seconds = hours * 3600
minutes_seconds = minutes * 60
total_seconds = hour_seconds + minutes_seconds + seconds
print ("The total amount of seconds in the time length you provided is", total_seconds)

