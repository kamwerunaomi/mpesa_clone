import datetime
class SavingsAccount:
	def __init__(self):
		self.name=input("Please Enter Your Name")
		self.phone_number=input("Please Enter Your Phone Number")	
		print("Welcome {}.".format(self.name))	
		print("Start by depositing some money")
		self.balance=500
		self.deposits=[]
		self.withdrawals=[]
	def deposit_cash(self, amount):
		if amount < 0:
			print("Invalid Deposit Amount ")
		else:
			self.balance+=amount
			print("Your balance is{}".format(self.balance))
			deposits_details={"time":datetime.datetime.now(),"amount":self.balance}
			self.deposits.append(deposits_details)	
	def show_balance(self):
		print("Dear {} your current balance is {}".format(self.name,self.balance))
	def withdraw_cash(self,amount):
		if amount <500:
			print("You cant withdraw less than 500 shillings")
		elif amount > self.balance:
			print("Cannot withdraw beyond the minimum account balance")
		else:
			self.balance-=amount
			print("Your balance is {} ".format(self.name, self.balance))
			withdrawals_details={"time":datetime.datetime.now(),"amount":self.balance}
			self.withdrawals.append(withdrwals_details)
	def show_deposits(self):
		for deposit in self.deposits:
			print("Dear {} on {} you deposited {} and your account balance is {}".format(self.name,deposit["time"].strftime("%c"),deposit["amount"],self.balance))
	def show_withdrawals(self):
		for withdrawal in self.withdrawals:
			print("Dear {} on {} you deposited {} and your account balance is {}".format(self.name,deposit["time"].strftime("%c"),deposit["amount"],self.balance))
