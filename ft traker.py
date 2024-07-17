#financial_tracker.py
#main page function
def display_menu():
    print('personal finance tracker')
    print('='*25)
    print('1. View Transactions')
    print('2. Add income')
    print('3. Add Expense')
    print('4. View Summary')
    print('5. Exit')
    


#transaction functionality
    
def view_transactions():
    try:
        with open("transactions.txt", "r") as file:
            transactions = file.readlines()
            if not transactions:
                print("No transactions recorded.")
            else:
                print("Transactions:")
                for transaction in transactions:
                    print(transaction.strip())
    except FileNotFoundError:
        print("No transactions recorded.")
        
#add income function

def add_income():
        amount= input('Enter income amount: ')
        category= input('enter income category: ')
        with open('transactions.txt', 'a') as file:
            file.write(f"Income: {amount}-{category}\n")
        print(f"Income of {amount} added in {category} category.")

#add expense function

def add_expense():
    amount = input("Enter expense amount: ")
    category = input("Enter expense category: ")
    with open("transactions.txt", "a") as file:
        file.write(f"Expense: {amount} - {category}\n")
    print(f"Expense of {amount} added in {category} category.")

#view summary function


def view_summary():
    try:
        with open("transactions.txt", "r") as file:
            transactions = file.readlines()
            income_total = 0
            expense_total = 0
            for transaction in transactions:
                if "Income" in transaction:
                    amount = float(transaction.split("-")[0])
                    income_total += amount
                elif "Expense" in transaction:
                    amount = float(transaction.split("-")[0])
                    expense_total += amount
            print(f"Total Income: {income_total}")
            print(f"Total Expenses: {expense_total}")
            print(f"Net Savings: {income_total - expense_total}")
    except FileNotFoundError:
        print("No transactions recorded.")


#user input function
    
def main():
    while True:
        display_menu()
        choice=input('Enter your choice: ')
        if choice=='1':
            view_transactions()
        elif choice=='2':
            add_income()
        elif choice=='3':
            add_expense()
        elif choice=='4':
            view_summary()
        elif choice=='5':
            print('Thankyou, visit again')
            print('Goodbye!')
            break
        else:
            print('Invalid Choice, Please try again.')
if __name__=="__main__":
    main()


  

