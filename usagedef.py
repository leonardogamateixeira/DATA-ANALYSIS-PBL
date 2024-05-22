from datetime import datetime
from datetime import timedelta
from tabulate import tabulate
import csv

def DayAdd():
    date = datetime.strptime("%d/%m/%Y")
    dateplus = date + timedelta(days=1)
    return dateplus.strftime("%d/%m/%Y")

def ConvertDate(date):
    dt = date[0].split('/')
    return datetime(
        int(dt[2]),
        int(dt[1]),
        int(dt[0]),
    )