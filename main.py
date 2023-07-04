from sales_processor import process_sales_data

# Specifing the path to the sales data CSV file(sales_data.csv is the name of the file where the sales data is stored)
csv_file = 'sales_data.csv'

# Processing the sales data(doing the calculations using the sales data from the file)
total_sales = process_sales_data(csv_file)

# Displaying the total sales
print(f'Total sales: ${total_sales:.2f}')
#The .2 is a formatting specifier. ' :.2f' means it's a float number with two decimal places. The number is rounded to two decimal places.
