import csv
#the function that does the actual calculations(reads the sales data and calculates the amount)
#csv_file is the sales data file.
def process_sales_data(csv_file):
    total_sales = 0

#The 'r' inside the parentheses is a special code that tells Python that we want to open the file for reading, without writing or changing anything.
# 'open()' is for accessing the file's content.
# The 'with' statement ensures that the file is properly closed after we finish using it.
#The 'csv.DictReader(file)' function is a tool that helps us read 'CSV' files, which are files that store tabular data (like a table) with values separated by commas.
#In this line sales_amount = float(row['Sales']) : It takes the price written as a word and changes it into a number if we need to convert it to a number so we can add it up.
#So we use row['Sales'] to get the value of the 'Sales' column for that item.    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales_amount = float(row['Sales'])
            total_sales += sales_amount

    return total_sales
