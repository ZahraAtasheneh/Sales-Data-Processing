import csv

def process_sales_data(csv_file):
    total_sales = 0

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales_amount = float(row['Sales'])
            total_sales += sales_amount

    return total_sales
