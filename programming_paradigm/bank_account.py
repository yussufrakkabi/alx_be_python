class BankAccount:
  """
  A simple BankAccount class for deposit, withdraw, and balance display operations.
  """

  def __init__(self, initial_balance=0.0):
    """
    Initializes a BankAccount object with an optional starting balance.

    Args:
        initial_balance (float, optional): The starting balance. Defaults to 0.0.
    """
    self.account_balance = initial_balance

  def deposit(self, amount):
    """
    Deposits the specified amount to the account balance.

    Args:
        amount (float): The amount to deposit.

    Raises:
        ValueError: If the deposit amount is negative.
    """
    if amount < 0:
      raise ValueError("Deposit amount cannot be negative.")
    self.account_balance += amount

  def withdraw(self, amount):
    """
    Attempts to withdraw the specified amount from the account balance.

    Args:
        amount (float): The amount to withdraw.

    Returns:
        bool: True if the withdrawal is successful, False otherwise.  

    """
    if amount > self.account_balance:
      return False
    self.account_balance -= amount
    return True

  def display_balance(self):
    """
    Prints the current account balance in a user-friendly format.
    """
    print(f"Current Balance: ${self.account_balance:.2f}")
