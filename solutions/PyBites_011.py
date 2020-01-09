'''
Bite 11. Enrich a class with dunder methods ☆
Let's enrich an Account class by adding dunder (aka special) methods to support the following:

1. length of the object: len(acc) returns the number of transactions
2. account comparison: acc1 >,<,>=.<=,== acc2 returns a boolean comparing account balances
3. indexing: acc[n] shows the nth transaction onaccount (0 based)
iteration: list(acc) returns a sequence of account transactions
4. operator overloading: acc + int and acc - int can be used to add/subtract money
5. string representation: str(acc) returns NAME account - balance: INT

Good luck!
'''

from functools import total_ordering

@total_ordering
class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def _validate(self, amount):
        if not isinstance(amount, int):
            raise ValueError('needs an int')
            
    # add dunder methods below
    def __len__(self):
        return len(self._transactions)
        
    def __eq__(self, x):
        return self.balance== x.balance
        
    def __lt__(self, x):
        return self.balance < x.balance
        
    def __getitem__(self, index):
        return self._transactions[index]
    
    def __add__(self, other):
        self._validate(other)
        self._transactions.append(other)

    def __sub__(self, other):
        self._validate(other)
        self._transactions.append(-other)
        
    def __repr__(self):
        return f'{self.name} account - balance: {self.balance}'
