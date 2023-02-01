from the_bank import Bank
from account import Account

Account1 = Account("haytham",value=100,address="home",zipp=1301)
Account2 = Account("haytham2",value=50,address="homae",zipp=13201)
bank = Bank()
bank.add(Account1)
bank.add(Account2)
bank.transfer(Account1 ,Account2, 30)
print(Account2.value)
print(Account1.value)

