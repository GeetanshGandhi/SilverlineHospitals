#Billing details
import mysql.connector as m
from n3days_per_room import *

def generate_bill():
    days_list = list(days_per_room(1))
    total_days = days_list[1] + days_list[2] + days_list[3] + days_list[4]
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor(buffered = True)
    # data-fetching
    patient_id = days_list[0]
    query = "select Patient_Name, Bill_Number, Treatment_Id,"\
            "Insurance_Number,Doctor_Id from patients where Patient_Id = '{}'".format(patient_id)
    line.execute(query)
    res = line.fetchone()

    patient_name = res[0]
    bill_id = res[1]
    trt_id = res[2]
    doc_id = res[4]
    insure = res[3]

    query = "select * from treatment where Treatment_Id = '{}'".format(trt_id)
    line.execute(query)
    res5 = line.fetchone()
    trt_name = res5[1]
    surgery = res5[5]

    if surgery == 1:
        surgery_time = res5[6]
        surgery_charges = surgery_time*5000
        trt_cost = res5[4]
    else:
        surgery_charges = 0
        trt_cost = res5[4]*total_days

    # Room cost
    pr_cost = days_list[1]*3500
    sr_cost = days_list[2]*2700
    gwb_cost = days_list[3]*2500
    icu_cost = days_list[4]*6000
    room_cost = pr_cost + sr_cost + gwb_cost + icu_cost

    # visiting charges
    query = "select Visit_Charges from doctors where Doctor_Id = '{}'".format(doc_id)
    line.execute(query)
    res4 = line.fetchone()
    visit_charges = int(res4[0]) * total_days

    # food cost
    service_charges = 1000 * total_days

    # total Cost
    cost_wo_tax = trt_cost + room_cost + visit_charges + service_charges + surgery_charges
    tax = cost_wo_tax * 0.18
    total_cost = cost_wo_tax + tax
    pmethodlist = ['Cash','Cheque','NEFT','IFSC','Online','Insurance','Loan']
    print('Here are the available modes of payment:')
    count = 1
    numlist = []
    for i in range(len(pmethodlist)):
        print('%d) '%count,pmethodlist[i])
        count+=1
        numlist.append(str(i+1))

    p_method_inp = input("Please enter the number alongside the preferred method:\n")
    while p_method_inp not in numlist or p_method_inp.isdigit()==False:
        p_method_inp = input('Invalid Choice, Kindly Re-Enter!\n')
    else:
        p_method_inp = int(p_method_inp)
    p_method = pmethodlist[p_method_inp-1]
    reg_fees = 2000
    # table!!
    query = "insert into bill_details(Patient_Id, Bill_number,Patient_Name,Treatment_Name,Treatment_Id," \
            "Doctor_Id, Registeration_Fees,Treatment_Cost,Room_Cost,Service_Charges,Visit_Charges,"\
            "Surgery_Charges,Insurance_Number,Total,Tax,Grand_Total,Payment_Method,Status) "\
            "values('{}','{}','{}','{}','{}','{}',{},{},{},{},{},{},'{}',{},{},{},'{}',{})".format(patient_id.upper(), bill_id,
            patient_name, trt_name, trt_id, doc_id, reg_fees, trt_cost, room_cost, service_charges, visit_charges,surgery_charges,
            insure,cost_wo_tax, tax,total_cost,p_method,0)
    line.execute(query)
    con.commit()
    line.close()
    con.close()
    return patient_id.upper() , reg_fees, trt_cost, room_cost, service_charges, visit_charges,surgery_charges, tax,total_cost