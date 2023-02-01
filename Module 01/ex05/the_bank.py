class Bank(object):
	def __init__(self):
		self.accounts = []

	@staticmethod
	def is_valid(account):
		if not len(account.__dict__) % 2:
				raise Exception("corrupted.")
		z = 0
		a = 0
		name = 0
		id_ = 0
		value = 0
		for k,v in account.__dict__.items():
			if k[0] == 'b':
				raise Exception("corrupted.")
			if k.startswith('zip'):
				z = 1
			if k.startswith('addr'):
				a = 1
			if k == 'name':
				name = 1
				if not isinstance(v,str):
					raise Exception("corrupted.")
			if k == 'id':
				id_ = 1
				if not isinstance(v,int):
					raise Exception("corrupted.")
			if k == 'value':
				value = 1
				if not isinstance(v,float) and not isinstance(v,int):
					raise Exception("corrupted.")
		if not z or not a or not name or not id_ or not value:
			raise Exception("corrupted.")
	def add(self, new_account):
		Bank.is_valid(new_account)
		self.accounts.append(new_account)
	def transfer(self, origin, dest, amount):
		Bank.is_valid(origin)
		Bank.is_valid(dest)
		if origin.value < amount:
			raise Exception("Not enough money.")
		origin.transfer(-amount)
		dest.transfer(amount)
	# def fix_account(self, name):


# from account import Account
# class Bank:
# 	def __init__(self, account,**kwargs):
# 		self.__dict__.update(kwargs)
# 		if not isinstance(Account,account):
# 			raise Exception("Not the right object.")
# 		# if not hasattr(self, 'amount'):
# 		# 	self.amount = 0
# 		# if account.value < self.amount:
# 		# 	raise Exception("not enough money.")
# 		# else:
# 		# 	account.transfer(self.amount)
# 		if not len(account.__dict__) % 2:
# 			raise Exception("corrupted.")
# 		z = 0
# 		a = 0
# 		name = 0
# 		id_ = 0
# 		value = 0
# 		for k,v in account.__dict__.items():
# 			if k[0] == 'b':
# 				raise Exception("corrupted.")
# 			if k.startswith('zip'):
# 				z = 1
# 			if k.startswith('addr'):
# 				a = 1
# 			if k == 'name':
# 				name = 1
# 				if not isinstance(v,str):
# 					raise Exception("corrupted.")
# 			if k == 'id':
# 				id_ = 1
# 				if not isinstance(v,int):
# 					raise Exception("corrupted.")
# 			if k == 'value':
# 				value = 1
# 				if not isinstance(v,float) and not isinstance(v,int):
# 					raise Exception("corrupted.")


