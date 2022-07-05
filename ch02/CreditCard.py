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


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        """Create a new predatory credit card instance"""
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5  # use mutators instead
        return success

    def process_month(self):
        if self.get_balance() > 0:
            monthly_factor = pow(1 + self._apr, 1/2)
            self._balance *= monthly_factor


if __name__ == '__main__':
    wallet = [CreditCard('John Thomas', 'California Savings', '5391 0375 9387 5309', 2500),
              CreditCard('John Thomas', 'California Federal', '5391 0375 4532 5223', 3500),
              CreditCard('John Thomas', 'California Finance', '5391 3233 3266 1355', 5000)]

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print(f'Customer = {wallet[c].get_customer()}')
        print(f'Bank= {wallet[c].get_bank()}')
        print(f'Account= {wallet[c].get_account()}')
        print(f'Limit= {wallet[c].get_limit()}')
        print(f'Balance= {wallet[c].get_balance()}')

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print(f'New Balance: {wallet[c].get_balance()}')
        print()
