import datetime

def calculate_monthly_installments(installments_expenses):
    """
    Calculate and shows a summary of installments expenses.

    Args:
        installments_expenses (list): each element represents an expense in installments with the
                                      format (amount_per_installment, current_installment, total_installments).
                                      example: [(100, 1, 6), (50, 3, 12)].

    Returns:
        None
    """
    
    # Get today's date
    today = datetime.date.today()
    
    # find the maximum number of total installments to determine the range of months to consider
    max_installment_total = 0
    for expense in installments_expenses:
        remaining_installments = expense[2] - expense[1] + 1
        if remaining_installments > max_installment_total:
            max_installment_total = remaining_installments
    
    # Diccionario para almacenar los totales por mes
    monthly_totals = {}

    # Distribute each expense over its remaining installments
    for amount, current_installment, total_installments in installments_expenses:
        # Calculate remaining installments
        remaining_installments = total_installments - current_installment + 1
        
        # Propagate the amount to the corresponding months
        for i in range(remaining_installments):
            # Calculate the month and year for the installment
            expense_month = today.month + i
            expense_year = today.year
            
            # if month exceeds December, adjust year and month
            if expense_month > 12:
                expense_month -= 12
                expense_year += 1
            
            # format key as 'YYYY-MM'
            mes_key = f"{expense_year:04d}-{expense_month:02d}"
            
            # Add the amount to the corresponding month
            if mes_key in monthly_totals:
                monthly_totals[mes_key] += amount
            else:
                monthly_totals[mes_key] = amount

    # Sorts the months
    sorted_months = sorted(monthly_totals.keys())
    
    # Print the summary
    print("--- Monthly Expenses Summary ---")
    for month in sorted_months:
        total_amount = monthly_totals[month]
        print(f"Month: {month}, Amount: ${total_amount:,.2f}")
    print("-----------------------------------")