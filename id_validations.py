from mysql import connector as m

def pid_valid(pid_val_small):
    pid_val = pid_val_small.upper()
    con = m.connect(host = "localhost", user = "root", password = "mysql", database = "silverline_hospital")
    line = con.cursor()
    query1 = "select Patient_Id from patients"
    line.execute(query1)
    res1 = line.fetchall()
    curpatients = []
    for i in range(len(res1)):
        curpatients.append(res1[i][0])

    query2 = "select Patient_Id from discharged_patients"
    line.execute(query2)
    res2 = line.fetchall()
    dispatients = []
    for i in range(len(res2)):
        dispatients.append(res2[i][0])
    while pid_val not in curpatients:
        pid_val_reinp = input("Invalid Patient ID (no such patient or the patient has already been discharged)\nRe-Enter\n")
        pid_val = pid_val_reinp.upper()
    else:
        return pid_val

def bid_valid(bid_val_small):
    bid_val = bid_val_small.upper()
    con = m.connect(host="localhost", user="root", password="mysql", database="silverline_hospital")
    line = con.cursor()
    query1 = "select Bill_Number from Bill_Details"
    line.execute(query1)
    res1 = line.fetchall()
    allbills = []
    for i in range(len(res1)):
        allbills.append(res1[i][0])
    while bid_val not in allbills:
        bid_val_small = input("Invalid Bill NumberRe-Enter\n")
        bid_val = bid_val_small.upper()
    return bid_val