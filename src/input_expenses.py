from entities.expenses import Expense


def input_expenses():

    #Gets and validates date    
    expense_date = input("Date: ")
    #Gets and validates amount
    expense_amount = input("Amount: ")
    #Gets and validates installments
    installments_not_valid = True
    while (installments_not_valid):
        expense_installments = input("Installments: ")
        if (expense_installments.isnumeric()):
            installments_not_valid = False
    
    new_expense = Expense(expense_date, expense_amount, expense_installments)
    print(new_expense)

    return
