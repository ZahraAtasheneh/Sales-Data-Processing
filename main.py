from sales_processor import process_sales_data

# Specifing the path to the sales data CSV file
csv_file = 'sales_data.csv'

# Processing the sales data
total_sales = process_sales_data(csv_file)

# Displaying the total sales
print(f'Total sales: ${total_sales:.2f}')
