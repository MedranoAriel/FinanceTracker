from calculate_monthly_installments import calculate_monthly_installments
from menu import generate_menu
from input_expenses import input_expenses

# --- Examples ---
# Format: (amount per installment, current installment, total installments)
my_expenses = [
    (31916.74, 2, 12),   
    (20000.00, 3, 6),
    (35582.43, 3, 3),
    (32770.00, 4, 6), 
    (6500.00, 4, 6),
    (45650.00, 4, 12),
    (6333.00, 4, 6)
]

def main():

    #initialize user choice
    user_choice = '0'

    while user_choice != '3':
        # Prints the menu and options
        generate_menu()
        # Obtain user input
        user_choice = input("Enter your choice: ")
        
        #Verify the user choice and call the correponding funcion
        if user_choice == '1':
            # Calculate and display the monthly installments summary
            calculate_monthly_installments(my_expenses)
        elif user_choice == '2':
            input_expenses()
        elif user_choice == '3':
            print("Thanks for using the app! Goodbye!")


if __name__ == "__main__":
    main()

