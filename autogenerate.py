#this file generates various IDs
import mysql.connector as m
from list_dict import *
''' The mechanism of the following functions given below 
 is(except r_id)-
 1.Searching of the maximum value from the table-
   a.If not available than assigning a default value
   b.If available then -
     i.Slicing the maximum value(alphanumeric) to 
       extract only numeric part from it and 
       converting it to integer.
    ii.Adding 1 to integer value to get the next number 
       and then converting it back to string
   iii.Concatenating this string to the original string 
       and returning the value'''
def autogen_bid():  #generation of new bill number
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor()
    query = "select max(Bill_Number) from patients"
    line.execute(query)
    res = list(line.fetchone())
    query1 = "select max(Bill_Number) from discharged_patients"
    line.execute(query1)
    res1 = list(line.fetchone())
    res2 = [None, None]
    res.extend(res1)
    if res == res2:
        Bill_Number = '1BD0001'
    else:
        if res[0] is None:
            x = int(res[1][3::])
            y = str(1 + x)
            if len(y) == 2:
                Bill_Number = res[1][0:5] + y
            elif len(y) == 3:
                Bill_Number = res[1][0:4] + y
            else:
                Bill_Number = res[1][0:6] + y
        elif res[1] is None:
            x = int(res[0][3::])
            y = str(1 + x)
            if len(y) == 2:
                Bill_Number = res[0][0:5] + y
            elif len(y) == 3:
                Bill_Number = res[0][0:4] + y
            else:
                Bill_Number = res[0][0:6] + y
        else:
            if res[0][3::] > res[1][3::]:
                x = int(res[0][3::])
                y = str(1 + x)
                if len(y) == 2:
                    Bill_Number = res[0][0:5] + y
                elif len(y) == 3:
                    Bill_Number = res[0][0:4] + y
                else:
                    Bill_Number = res[0][0:6] + y
            elif res[0][3::] < res[1][3::]:
                x = int(res[1][3::])
                y = str(1 + x)
                if len(y) == 2:
                    Bill_Number = res[1][0:5] + y
                elif len(y) == 3:
                    Bill_Number = res[1][0:4] + y
                else:
                    Bill_Number = res[1][0:6] + y
    line.close()
    con.close()
    return Bill_Number.upper()

def autogen_pid():  #generation of new patient ID
    patient_id = ''
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor()
    query = "select max(Patient_Id) from patients"
    line.execute(query)
    res = list(line.fetchone())
    query1 = "select max(Patient_Id) from discharged_patients"
    line.execute(query1)
    res1 = list(line.fetchone())
    res2 = [None, None]
    res.extend(res1)
    if res == res2:
        patient_id = '1AD0001'
    else:
        if res[0] is None:
            x = int(res[1][3::])
            y = str(1 + x)
            if len(y) == 2:
                patient_id = res[1][0:5] + y
            elif len(y) == 3:
                patient_id = res[1][0:4] + y
            else:
                patient_id = res[1][0:6] + y
        elif res[1] is None:
            x = int(res[0][3::])
            y = str(1 + x)
            if len(y) == 2:
                patient_id = res[0][0:5] + y
            elif len(y) == 3:
                patient_id = res[0][0:4] + y
            else:
                patient_id = res[0][0:6] + y
        else:
            if res[0][3::] > res[1][3::]:
                x = int(res[0][3::])
                y = str(1 + x)
                if len(y) == 2:
                    patient_id = res[0][0:5] + y
                elif len(y) == 3:
                    patient_id = res[0][0:4] + y
                else:
                    patient_id = res[0][0:6] + y
            elif res[0][3::] < res[1][3::]:
                x = int(res[1][3::])
                y = str(1 + x)
                if len(y) == 2:
                    patient_id = res[1][0:5] + y
                elif len(y) == 3:
                    patient_id = res[1][0:4] + y
                else:
                    patient_id = res[1][0:6] + y
    line.close()
    con.close()
    return patient_id.upper()

def autogen_docid():    #generation of ID for new doctor
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor()
    query = "select max(Doctor_Id) from doctors"
    line.execute(query)
    res = line.fetchone()
    res1 = list(res)
    res2 = [None]
    if res1 == res2:
        doctor_id = "D001"
    else:
        x = int(res[0][1::])
        y = str(1 + x)
        if len(y) == 2:
            doctor_id = res[0][0:2] + y
        elif len(y) == 3:
            doctor_id = res[0][0:1] + y
        else:
            doctor_id = res[0][0:3] + y
    line.close()
    con.close()
    return doctor_id.upper()

def autogen_tid():  #generation of ID for new treatment
    treatment_id = ''
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor()
    query = "select DISTINCT(Category) from treatment"
    line.execute(query)
    res = line.fetchall()
    trtlist = []
    print("Following are the categories available for treatments:-")
    for i in res:
        trtlist.append(i[0])
        print(i[0])
    print(trtlist)
    new = input('Do you want to create a new category for the treatment?(y/n)')
    while new != 'n' and new != 'N' and new != 'y' and new != 'Y':
        new = input('Invalid choice, Please re-enter!(y/n)')
    if new == 'N' or new == 'n':
        trt_cat = input('enter treatment category(make sure you use correct capitalization:\n')
        while trt_cat not in trtlist:
            trt_cat = input('Invalid Treatment Category!! Please Re-Enter. If want to create new category, Press 1!')
            if trt_cat == 1:
                new = 'Y'
                break
        for i in range(len(res)):
            if trt_cat == res[i][0]:
                query1 = "select max(Treatment_id) from treatment where category='{}'".format(res[i][0])
                line.execute(query1)
                res1 = line.fetchone()
                x_end = int(res1[0][3::])
                x_start = str(res1[0][0:3])
                y = str(1 + x_end)
                if len(y) == 2:
                    treatment_id = x_start + "0" + y
                elif len(y) == 3:
                    treatment_id = x_start + y
                else:
                    treatment_id = x_start + "00" + y

    elif new == 'Y' or new == 'y':
        trt_cat = input('''Enter the treatment category as per the following capitalisations:
-->If abbreviation, Enter initial letters of category in BLOCK letters
-->If not abbreviation, Enter full-name with initial letters of each word in BLOCK\n''')
        check = input('You\'ve Entered %s as the category, press 1 to confirm or press 2 to Re_Enter'%trt_cat)
        while check == 2:
            trt_cat = input('''Enter the treatment category as per the following capitalisations:
-->If abbreviation, Enter initial letters of category in BLOCK letters
-->If not abbreviation, Enter full-name with initial letters of each word in BLOCK\n''')
            check = input('You\'ve Entered %s as the category, press 1 to confirm or press 2 to Re_Enter' % trt_cat)
        treatment_id = (trt_cat.capitalize())[0:3] + '001'

    line.close()
    con.close()
    return treatment_id.capitalize(), trt_cat


def autogen_userid():
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor()
    query = "select max(User_Id) from login"
    line.execute(query)
    res = line.fetchone()
    res1 = list(res)
    res2 = [None]
    if res1 == res2:
        user_id = "Adm01"
    else:
        x = int(res[0][3::])
        y = str(1 + x)
        if len(y) == 2:
            user_id = res[0][0:3] + y
        else:
            user_id = res[0][0:4] + y
    con.commit()
    line.close()
    con.close()
    return user_id.capitalize()

def autogen_rid(admission, category = None):
    roomno = ''
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor(buffered=True)
    if admission == False and category is None:
        query0 = "select DISTINCT(Room_Type) from room_details where Room_Type not like 'Operation Theatre'"\
        "and Availability = 0"
        line.execute(query0)
        res0 = line.fetchall()
        print('Following are the types of rooms available:')
        types = []  #fib series
        num = 1 #palindrome
        #numpy org modul
        for i in range(len(res0)):
            types.append(res0[i][0])
            print('%d) '%num, res0[i][0])
            num+=1
        type_inp_int = input("Enter the number alongside the required room:\n")
        while type_inp_int.isdigit()==False:
            type_inp_int = input('Invalid room type choice. Please Re-Enter:\n')
        numlist = []
        for j in range(1,num):
            numlist.append(j)
        while type_inp_int not in numlist:
            type_inp_int = int(input('Invalid room type choice. Please Re-Enter:\n'))
        type_inp = types[type_inp_int-1]
    else:
        type_inp = category
    query = "select * from room_details where Room_Type = '{}'".format(type_inp)
    line.execute(query)
    res = line.fetchall()
    for i in range(len(res)):
        if res[i][3] == 0:
            query1 = "select Room_Number from room_details where Room_Type = '{}'" \
                     "and Availability = 0".format(type_inp)
            line.execute(query1)
            res1 = line.fetchone()
            roomno = res1[0]
            break
    line.close()
    con.close()
    return roomno