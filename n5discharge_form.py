#discharge
import mysql.connector as m
from datetime import date
from n6bill_details import generate_bill
from list_dict import *
from tk4_bill_display import billdisplay
from n8bill_csv import csv_for_bill
from id_validations import pid_valid

def discharge():
    g_in = generate_bill()

    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor(buffered=True)
    p_id_in = g_in[0]
    p_id = pid_valid(pid_val_small=p_id_in)
    q1 = "select Patient_Name,AadharCard_Number,MobileNumber_Guardian, Treatment_Id,Doctor_Id," \
         "Date_Admission,Bill_Number, Room_Number from patients where Patient_Id = '{}'".format(p_id)
    line.execute(q1)
    res = line.fetchone()
    p_nm = res[0]
    adhar = res[1]
    mob = res[2]
    t_id = res[3]
    d_id = res[4]
    b_no = res[6]
    r_no = res[7]

    csv_for_bill(bill_number=b_no)
    date_adm = res[5]
    date_disch = date.today()
    n_days = str(date_disch - date_adm)
    if n_days == '0:00:00':
        no_of_days_int = 1
    elif n_days == '1 day, 0:00:00':
        no_of_days_int = 1
    else:
        n_days_r = n_days[-15::-1]
        n_days_sl = n_days_r[::-1]
        no_of_days_int = int(n_days_sl)

    query0 = "select Doctor_Name from doctors where Doctor_Id = '{}'".format(d_id)
    line.execute(query0)
    d_name = list(line.fetchone())[0]
    query = "insert into discharged_patients values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}'" \
            ")".format(p_id, p_nm, adhar, t_id, d_id, d_name, mob, date_adm, date_disch, no_of_days_int, b_no)
    line.execute(query)

    query2 = "update room_details set Availability = 0, Patient_Id = NULL, Doctor_Id = NULL where Room_Number = '{}'".format(
        r_no)
    line.execute(query2)
    query3 = "delete from patients where Patient_Id = '{}'".format(p_id)

    query4 = "select max(Date_of_Change) from change_transaction where Patient_Id = '{}'".format(p_id)
    line.execute(query4)
    res1 = line.fetchone()

    change_final = date_disch - res1[0]
    change_final_str = str(change_final)
    if change_final_str == '0:00:00':
        change_final_int = 0
    elif change_final_str == '1 day, 0:00:00':
        change_final_int = 1
    else:
        slice1 = change_final_str[-15::-1]
        reverse = slice1[::-1]
        change_final_int = int(reverse)
    query5 = "update change_transaction set Number_of_Days = {} where Patient_Id = '{}' and " \
             "Number_of_Days =0".format(change_final_int, p_id)
    line.execute(query5)
    line.execute(query3)
    con.commit()
    line.close()
    con.close()
    billdisplay(b_id_input=b_no)