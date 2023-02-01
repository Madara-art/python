import os
import csv

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
	def __enter__(self):
		try:
			self.filename = open(self.filename,'r')
		except FileNotFoundError:
			print("F for this file.")
			return None
		except PermissionError:
			print("This file is out of ur league like all the girls.")
			return None
		df = csv.reader(self.filename,delimiter=self.sep)
		in_ = 0
		for r in df:
			if in_ == 0:
				in_ = 1
				cnt = len(r)
			else:
				if cnt != len(r):
					return None
		return self

	def __exit__(self, exc_type, exc_value, exc_tb):
		if exc_type:
			print(f"An error occurred: {exc_value}")
		self.filename.close()
	def getdata(self):
		self.filename.seek(0)
		df = csv.reader(self.filename,delimiter=self.sep)
		lst = []

		for r in df:
			lst.append(r)
		for _ in range(self.skip_top):
			lst.remove(lst[0])
		for _ in range(self.skip_bottom):
			if not lst:
				print("invalid skip_top/bottom values")
				return []
			lst.remove(lst[-1])
		return lst
	def getheader(self):
		self.filename.seek(0)
		df = csv.reader(self.filename,delimiter=self.sep)
		for r in df:
			return r
# with CsvReader("file.csv") as file:
# 	if file == None:
# 		print("File is corrupted")
# 		exit(1)
# 	a = file.getdata()

# 	print(a)
