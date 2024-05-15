import mysql.connector as m
from datetime import date, timedelta
from id_validations import pid_valid

def up_roomno():
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor()
    line1 = con.cursor()
    roomno = ''
    p_id_in = input('Enter Patient ID:\t')
    p_id = pid_valid(p_id_in)
    p_id = p_id.upper()

    query3 = "select Room_Number from change_transaction where Patient_Id = '{}'".format(p_id)  #
    line.execute(query3)  
    res2 = line.fetchall()  
    prev_room_no = []
    for i in range(len(res2)):  
        prev_room_no.append(res2[i][0])  
        length = len(prev_room_no)

    query0 = "select max(Date_of_Change) from change_transaction where Patient_Id = '{}'".format(p_id)
    line.execute(query0)
    res0 = line.fetchone()
    if res0[0] == date.today():
        print("Sorry! A patient cannot change his/her room twice a day. "
              "Contact administration for emergency")
        return 0

    query = "select Room_Number,Doctor_Id from patients where Patient_Id = '{}'".format(p_id)
    query2 = "select room_Type from room_details where Patient_Id= '{}'".format(p_id)
    line.execute(query2)
    res = line.fetchone()
    line.execute(query)
    res10 = line.fetchone()
    print("The current Room Type is ", res[0])
    p_details = list(res10)
    docid = p_details[1]
    cur_room_no = p_details[0]
    n = 1
    while n == 1:
        query0 = "select DISTINCT(Room_Type) from room_details where Room_Type not like 'Operation Theatre'" \
                 "and Availability = 0"
        line.execute(query0)
        res0 = line.fetchall()
        print('Following are the types of rooms available:')
        types = []
        num = 1
        numlist = []
        for i in range(len(res0)):
            types.append(res0[i][0]) #[pr,sr,icu,gwb]
            print('%d) ' % num, res0[i][0])
            numlist.append(num) #(1,2,3,4)
            num += 1

        type_inp_int = input("Enter the number alongside the required room:\n")

        while ((type_inp_int.isdigit() == False) or (int(type_inp_int) not in numlist)) or \
                (types[int(type_inp_int)-1] == res[0]):
            type_inp_int = input('Invalid room type type input. Please Re-Enter:\n')

        else:
            type_inp = types[int(type_inp_int) - 1]
            query = "select * from room_details where Room_Type = '{}'".format(type_inp)
            line.execute(query)
            res = line.fetchall()
            for i in range(len(res)):
                if res[i][3] == 0:
                    for j in range(length):
                        query1 = "select Room_Number from Room_Details where Room_Type = '{}' "  \
                        "and Availability = 0 and Room_Number != '{}'".format(type_inp, prev_room_no[j])
                        line1.execute(query1)
                        res1 = line1.fetchall()
                        roomno = res1[0][0]
                        break

        query2 = "update room_details set Patient_Id = NULL, Availability = 0,Doctor_Id = NULL " \
                 "where Room_Number='{}'".format(cur_room_no)
        line.execute(query2)

        query3 = "update room_details set Patient_Id='{}', Availability = 1,Doctor_Id = '{}'" \
                 "where Room_Number='{}'".format(p_id, docid, roomno)
        line.execute(query3)

        query4 = "select max(Date_of_Change) from change_transaction where Patient_Id = '{}'".format(p_id)
        line.execute(query4)
        change = line.fetchone()

        prev_days = str(date.today() - change[0])
        if prev_days == '0:00:00':
            prev_days_int = 1
        elif prev_days == '1 day, 0:00:00':
            prev_days_int = 1
        else:
            prev_days_r = prev_days[-15::-1]
            prev_days_sl = prev_days_r[::-1]
            prev_days_int = int(prev_days_sl)

        query5 = "update change_transaction set Number_of_Days = {} where Date_of_Change = " \
                 "'{}' and Patient_Id = '{}'".format(prev_days_int, change[0], p_id)
        line.execute(query5)

        if change == date.today():
            query6 = "update change_transaction set Date_of_Change = '{}' where " \
                     "Patient_Id = '{}' and Date_of_Change = '{}'".format(date.today() + timedelta(1), p_id,
                                                                          date.today())
            line.execute(query6)
        else:
            query6 = "insert into change_transaction(Patient_Id,Room_Number,Date_of_Change,Number_of_Days)" \
                     "values('{}','{}','{}',{})".format(p_id, roomno, date.today(),1)
            line.execute(query6)

        query7 = "update patients set Room_Number='{}' where " \
                 "Patient_Id='{}'".format(roomno, p_id)
        line.execute(query7)
        print('Room type has been changed to - ', type_inp)
        print('Patient\'s new room number:\t', roomno)
        n = 0
    con.commit()
    line.close()
    line1.close()
    con.close()
