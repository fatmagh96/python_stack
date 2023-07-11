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

    # __refs__ = defaultdict(list)

    # @classmethod
    # def get_instances(cls):
    #     refs = []
    #     for ref in cls.__refs__[cls]:
    #         instance = ref()
    #         if instance is not None:
    #             refs.append(ref)
    #             yield instance
    #     # print(len(refs))
    #     cls.__refs__[cls] = refs

account1 = BankAccount(0.01,1000)
account2 = BankAccount(0.03)

account1.deposit(200).deposit(500).deposit(50).withdraw(899).yield_interest().display_account_info()

account2.deposit(100).deposit(350).withdraw(200).withdraw(100).withdraw(20).withdraw(300).yield_interest().display_account_info()
# print(account2.balance)

BankAccount.print_all_instances()