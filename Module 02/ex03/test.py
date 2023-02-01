from csvreader import CsvReader

if __name__ == "__main__":
	with CsvReader('file.csv') as file:
		data = file.getdata()
		header = file.getheader()
		print(data)
		print(header)