# import pandas as pd

# data = {'column_1': [1, 2, 3,4], 'column_2': ['A', 'B', 'C']}
# df = pd.DataFrame(data)

# df.to_csv('file.csv', index=False)
import csv

with open("file.csv", "r") as file:
	reader = csv.reader(file)

	print(reader[0])
	# print(shap(lst))