# Create a file with the User class, including the __init__ and make_deposit method
class User:
  def __init__(self, name, email):
    #attributes
    self.name = name
    self.email = email
    self.balance =0
    #methods
  def make_deposit(self, amount):
    self.balance += amount
    
    # Add a make_withdrawal method to the User class
  def make_withdrawal(self, amount):
    self.balance -= amount

    # Add a display_user_balance method to the User class  
  def display_user_balance(self):
    print(f"Balance: {self.balance}")
  def transfer_money(self, amount,reciever):
    self.make_withdrawal(amount)
    reciever.make_deposit(amount)

# Create 3 instances of the User class
john = User("John", "john@gmail.com")
jane = User("Jane", "jane@hotmail.com")
doe = User("Doe", "doe@yahoo.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
john.make_deposit(500)
john.make_deposit(700)
john.make_deposit(2000)

# john.make_withdrawal(80)

# john.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
jane.make_deposit(1200)
jane.make_deposit(300)

jane.make_withdrawal(400)
jane.make_withdrawal(100)

# jane.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance 
doe.make_deposit(5000)

doe.make_withdrawal(4000)
doe.make_withdrawal(300)
doe.make_withdrawal(300)

# doe.display_user_balance()


# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances


#Transfer money
john.transfer_money(1200, doe)

# john.display_user_balance()

# doe.display_user_balance()


