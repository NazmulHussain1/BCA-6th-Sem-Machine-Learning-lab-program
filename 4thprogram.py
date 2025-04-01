#4.Write a program to load and explore the dataset of CSV and Excell Files using pandas
import pandas as pd

#Load the CSV file
csv_file='C:/Users/nazmu/Desktop/Machine Learning Python/Sample.csv'
data_csv=pd.read_csv(csv_file)
print("csv file:")
print(data_csv)

#load the Excel file
excel_data=pd.read_excel('C:/Users/nazmu/Desktop/Machine Learning Python/sample_data.xlsx')
print("Excel_data:")
print(excel_data)

#basic Data exploration
print("\n  data Description")
print("CSV Data Description:")
print(data_csv.describe())

print("\nExcel Data Description:")
print(excel_data.describe())


#Displaying datatypes
print("\nDataTypes in csv file:")
print(data_csv.dtypes)

print("\n Datatypes in Excel file:")
print(excel_data.dtypes)
