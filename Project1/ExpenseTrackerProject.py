'''
Expense Tracker Project:

You are required to build a simple personal finance management tool. The
program should allow the user to:
 1. add an expense with details like date, category, description and amount
 2. view all recorded expenses in a clean format
 3.calculate total spending so far.
 4. exit the program gracefully when the user chooses to.

 all task must be implemented using loops, if-else, list and dictionary only. no user define function
 or file handling should be used.


'''

expenses=[] # list of expenses in form of dictionary
print("..............Welcome to Expense Tracker................")
while True:
    print("==== MENU ====")
    print("1. Add Expense")
    print("2. view all Expenses")
    print("3. view total Expense")
    print("4. Exit")

    choice=int(input("Please enter your choice : "))

# 1)..............Add expenses.........................

    if (choice ==1):
        date=input("Enter the date: ")
        category=input("Enter the category(loke food, travel, etc.) of your expense: ")
        description=input("Enter a short description: ")
        amount=float(input("Enter the total amount you spent: "))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expenses.append(expense)
        print("Expenses is Added Successfully.")

#2)...........view expenses...........................
    elif (choice ==2):
        if (len(expenses)==0):
            print("No Expenses Added.")
        else:
            print("==== This is your expenses ====")
            count=1
            for i in expenses:
                print(f"{count}:  {i["date"]},{i["category"]},{i["description"]},{i["amount"]}")
                count +=1

# 3)..........view total spending....................

    elif (choice ==3):
        total=0
        for i in expenses:
            total = total + i["amount"]
        print("\n Total amount is = ", total)

#4)....Exit................

    elif (choice ==4):
        print("Thank you for using our system.")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")




    
    
    


