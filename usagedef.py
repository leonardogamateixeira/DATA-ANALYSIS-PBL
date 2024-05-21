from datetime import datetime
from tabulate import tabulate
import csv

def ConvertDate(date):
    dt = date.split('/')
    return datetime(
        int(dt[2]),
        int(dt[1]),
        int(dt[0]),
    )

def valDate(date):
    try:
        DateObj = datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

with open('denguedata.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    print(tabulate(reader, headers='firstrow', tablefmt='rounded_grid'))