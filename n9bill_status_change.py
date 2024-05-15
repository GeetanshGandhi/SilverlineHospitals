import mysql.connector as m
from id_validations import bid_valid
from n8bill_csv import csv_for_bill

def billstatus():
    con = m.connect(host = 'localhost', user = 'root', password = 'mysql', database = 'silverline_hospital')
    line = con.cursor()
    b_id_in = input('Enter BILL NUMBER whose status is to be changed:\n')
    b_id = bid_valid(b_id_in)
    query = "update bill_details set Status=1 where Bill_Number = '{}'".format(b_id)
    line.execute(query)
    con.commit()
    print('Status changes Successfully! Contact Admin to procure the new CSV file.')
    csv_for_bill(bill_number = b_id_in)