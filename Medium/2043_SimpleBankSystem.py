# Problem <2042> : Simple Bank System (Medium)
# URL: https://leetcode.com/problems/simple-bank-system/description/?envType=daily-question&envId=2025-10-26
# Description:
#   You have been tasked with writing a program for a popular bank that will automate 
#   all its incoming transactions (transfer, deposit, and withdraw). 
#   The bank has n accounts numbered from 1 to n. 
#   The initial balance of each account is stored in a 0-indexed integer array balance, 
#   with the (i + 1)th account having an initial balance of balance[i].
#   Execute all the valid transactions. A transaction is valid if:
#   The given account number(s) are between 1 and n, and
#   The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
#   Implement the Bank class:
#   Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
#   boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
#   boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
#   boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.
#
# Example 1:
#   Input: ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
#           [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
#   Output: [null, true, true, true, false, false]


from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.valid_account(account1) or not self.valid_account(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.valid_account(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid_account(account):
            return False
        if self.balance[account - 1] < money:
            return False

        self.balance[account - 1] -= money
        return True

bank = Bank([1000, 1500, 2000])

print(bank.withdraw(1, 500))   #  True
print(bank.transfer(2, 3, 1000))  #  True
print(bank.deposit(3, 200))    #  True
print(bank.withdraw(2, 1000))  #  False 

print(bank.balance)  # [500, 500, 3200]

# Time complexity: O(1), is constant