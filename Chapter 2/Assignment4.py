'''
Write a program that takes total bill amount and number of friends as input, 
calculate how much each person will pay and also print the data type of each variable used.

'''

total_bill= float(input( " Enter the total bill amount : "))
friends= int(input(" Enter the total number of friends : "))
pay_amount= total_bill/friends
print(" Each person have to pay: ",pay_amount)
print("Data type of the variable total_bill: ",type(total_bill))
print(" Data type of the variable friends: ", type(friends))
print("Data type of the variable pay_amount: ",  type(pay_amount))