# Zackary Raymond chapter 2 lesson 2. excersise-3  2-8-2018

#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25

hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
gross_pay = float(hours*rate)
print ('Pay: ' + str(gross_pay))
