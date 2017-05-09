import datetime
class MPESA:
	def deposit_cash(self, amount):
		if amount < 50:
			print("You cant deposit below 50 shillings")
		else:
			self.balance+=amount
			print("Your balance is{}".format(self.balance))
			deposits_details={"time":datetime.datetime.now(),"amount":self.balance}
			self.deposits.append(deposits_details)	
	def show_balance(self):
		print("Dear {} thank you for using mpesa your current balance is {}".format(self.name,self.balance))
	