'''
Take input in Celsius and print its equivalent in Fahrenheit and Kelvin...
( using explicit type conversion and arithmetic operators.)...

Fahrenheit = (C * 9/5)+ 32
Kelvin= C +273.15

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''
C= input("Enter any temperature value in Celsius:")
C= float(C)
F= (C * 9/5) + 32
K= C + 273.15
print("The equivalent temperature in Fahrenheit is :", F)
print("The equivalent temperature in Kelvin is :", K)

