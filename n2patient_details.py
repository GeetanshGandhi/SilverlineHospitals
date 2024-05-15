#Patient Details
import mysql.connector as m
from list_dict import *
from tk1_pdetails import *
from id_validations import pid_valid

def p_details():
    con = m.connect(host = 'localhost', user = 'root', password = 'mysql',database = 'silverline_hospital')
    line = con.cursor()
    p_id_in = input('Enter the Patient ID of the patient\n')
    p_id = pid_valid(p_id_in)
    q = "select * from patients where Patient_Id = '{}'".format(p_id)
    line.execute(q)
    res = line.fetchone()
    doc = doctors[res[7]][0]
    t_name = tname_gen[res[4]]
    patient_details(res[0], res[1], res[2], res[3], res[4], t_name, res[5], res[6],doc, res[8], res[9])
