class CreditCard:
    """A costumer credit card"""

    def __init__(self, customer, bank, account, limit):
        """Creates a new credit card instance"""
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the cusomer"""
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        """Charge given price to the card. Assuming sufficient credit limit"""

        if price + self._balance > self._limit:
            return False
        self._balance += price
        return True

    def make_payment(self, amount):
        self._balance -= amount
