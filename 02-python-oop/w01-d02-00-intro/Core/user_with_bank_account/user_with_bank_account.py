class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance=0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        # your code here
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else :
            self.balance -= amount
        return self
    
    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        return None
    
    def yield_interest(self):
        # your code here
        if self.balance >= 0:
            self.balance += self.balance*self.int_rate
        return self

    @classmethod
    def print_all_instances(cls):
        # cls.all_instances.append()
        for account in cls.all_accounts:
            account. display_account_info()
        
        return None
    

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount, self.account):
        # your code here
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return None
    
john = User("John","john@gmail.com")

john.make_deposit(500).make_withdrawal(200).display_user_balance()

