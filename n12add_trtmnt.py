import mysql.connector as m
from autogenerate import autogen_tid
from list_dict import *

def add_trt():
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor()
    trt_id = autogen_tid()
    trt_nm = input('Enter Treatment Name:\n')
    trt_nm_cap = trt_nm.title()
    d_inp = input('Doctor ID of Doctor undertaking\n')
    d = d_inp.upper()
    d_id = list(doctors.keys())
    while d not in d_id:
        d_inp = input("Invalid Doctor ID. Kindly Re-Enter!\n")
        d = d_inp.upper()
    else:
        docid = d
    cost = int(input('Enter Treatment\'s Cost:\n'))
    surgery_inp = input('Is surgery required for the treatment?(y/n)\n')
    surgery_inp_tinyint = 0
    while surgery_inp != 'n' and surgery_inp != 'N' and surgery_inp != 'y' and surgery_inp != 'Y':
        surgery_inp = input('Invalid Surgery detail. Please type \'yes\' or \'no\'\n')
    if surgery_inp == 'Y' or surgery_inp == 'y':
        surgery_inp_tinyint = 1
        surgeryhrs = float(input('Enter time required to perform surgery(in hours)'))
    else:
        surgery_inp_tinyint = 0
        surgeryhrs = 0

    query = "insert into treatment values('{}','{}','{}','{}',{},{},{})".format(trt_id[0], trt_nm_cap,
            trt_id[1], docid, cost, surgery_inp_tinyint,surgeryhrs)
    line.execute(query)
    con.commit()

    print('Entry Successful! the Treatment ID of the added treatment is', trt_id[0])
    line.close()
    con.close()