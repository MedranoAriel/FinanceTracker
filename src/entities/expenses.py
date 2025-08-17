class Expense:
    
    def __init__(self, date, amount, installments):
        self._date = date
        self._amount = amount
        self._installments = installments

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_installments(self):
        return self._installments

    def set_installments(self, installments):
        self._installments = installments

    def __str__(self):
        return f"Expense: - Date: {str(self._date)} - Amount: $ {str(self._amount)} - Installments: {str(self._installments)}" 