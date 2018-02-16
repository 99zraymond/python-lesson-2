# Zackary Raymond chapter 2 lesson 2. excersise-2  2-8-2018

#Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

celsius = float(input("Temp in Celsius: "))
fahr = celsius * (9.0/5.0) + 32

print ("Temp in Fahrenheit: %.2f" % fahr)