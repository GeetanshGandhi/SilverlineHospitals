import csv
import mysql.connector as m
from list_dict import doctors

def csv_for_bill(bill_number):
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor()
    col_list = 'bill_number,patient_id,patient_name,treatment_name,doctor_id,registeration_fees,treatment_cost,'\
                'room_cost,service_charges,visit_charges,surgery_charges,insurance_number,total,tax,grand_total,'\
                'payment_method,status'
    query = "select {} from bill_details where Bill_Number = '{}'".format(col_list,bill_number)
    line.execute(query)
    res = line.fetchone()
    for i in range(len(res)):
        if type(res[i]) == '<class \'str\'>':
            res[i] = str(res[i])
    path = 'csv_for_bill//'+res[0]+'.csv'
    file = open(path, 'w',newline = '\n')
    headlist = ['Bill Number','Patient ID','Patient Name','Treatment Name','Doctor Name',
                'Registration Fees','Treatment Cost (One time + Daily)','Room Cost','Service Charges',
                'Visit Charges','Surgery Charges','Insurance Number','Total','Tax','Grand Total',
                'Payment Method','Status(Current)']
    doctor_nm = doctors[res[4]][0]
    obj = csv.writer(file,delimiter =',')

    for i in range(len(headlist)):
        if i==4:
            obj.writerow([headlist[i],doctor_nm])
        elif i==10:
            if res[i] == '0':
                continue
            else:
                obj.writerow([headlist[i], res[i]])
        elif i==11:
            if res[i] is None:
                obj.writerow([headlist[i],'No Insurance'])
            else:
                obj.writerow([headlist[i], res[i]])
        elif i == 16:
            if res[i] == 0:
                obj.writerow([headlist[i], 'Due'])
            else:
                obj.writerow([headlist[i], 'Paid'])
        else:
            obj.writerow([headlist[i],res[i]])
    file.close()