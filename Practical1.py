import pandas as pd

#Load CSV file 
csv_file = pd.read_csv("data.csv")
print("CSV file data is")
print(csv_file)

#Explore CSV file 
print("\n First 5 Rows")
print(csv_file.head())

print("\n Columns Name")
print(csv_file.columns)

print("\n Data types")
print(csv_file.dtypes)

print("\n summary")
print(csv_file.describe())

# Load Excel File
# excel_file = pd.read_excel("data.xlsx", engine="openpyxl")
# print("\nExcel File Data:")
# print(excel_file)

# # Explore Excel File
# print("\nFirst 5 Rows:")
# print(excel_file.head())

# print("\nSummary:")
# print(excel_file.describe())