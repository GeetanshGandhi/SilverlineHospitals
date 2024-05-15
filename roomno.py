import mysql.connector as m
con = m.connect(host = 'localhost', user = 'root', password = 'mysql', database = 'silverline_hospital')
line = con.cursor()
l1 = []
pvtroom = []
for pvt1 in range(101, 131): 
    pvtroom.append(pvt1)
    l1.append(pvt1)
for pvt2 in range(201, 231): 
    pvtroom.append(pvt2)
    l1.append(pvt2)
shrroom = []
for shr in range(301, 326):
    alnum1 = str(shr) + '-A'
    alnum2 = str(shr) + '-B'
    shrroom.append(alnum1)
    shrroom.append(alnum2)
    l1.append(alnum1)
    l1.append(alnum2)
for shr2 in range(401, 426):
    alnum1 = str(shr2) + '-A'
    alnum2 = str(shr2) + '-B'
    shrroom.append(alnum1)
    shrroom.append(alnum2)
    l1.append(alnum1)
    l1.append(alnum2)
genward = []
for gen in range(601, 656):        #these numbers are bed number and NOT  room numbers
    genward.append(gen)
    l1.append(gen)
icu = []
for ic in range(501, 521):
    icu.append(ic)
    l1.append(ic)
ot = []
for ote in range(521,531,2):
    ot.append(ote)
    l1.append(ote)
roomdetails = {'Private Room' : [pvtroom, 3500],
'Shared Room': [shrroom, 2700],
'General Ward Bed': [genward, 2500],
'Intensive Care Unit': [icu, 6000],
'Operation Theatre': [ot]}
#print(roomdetails)
'''
for i in range(len(l1)):
    a = 0
    q1 = "insert into room_details(Room_Number, Availability) values('{}',{})".format(l1[i], a)
    line.execute(q1)
    con.commit()
    if l1[i] in pvtroom:
        q2 = "update room_details set Room_Type = \"Private Room\" where Room_Number between 101 and 130"
        q4 = "update room_details set Room_Cost = 3500 where Room_Number between 101 and 130"
        line.execute(q2)
        line.execute(q4)
        q3 = "update room_details set Room_Type = \"Private Room\" where Room_Number between 201 and 230"
        q5 = "update room_details set Room_Cost = 3500 where Room_Number between 201 and 230"
        line.execute(q3)
        line.execute(q5)
        con.commit()
    elif l1[i] in shrroom:
        q6 = "update room_details set Room_Type = \"Shared Room\" where Room_Number like '___-_'"
        q7 = "update room_details set Room_Cost = 2700 where Room_Number like '___-_'"
        line.execute(q6)
        line.execute(q7)
        con.commit()
    elif l1[i] in genward:
        q8 = "update room_details set Room_Type = \"General Ward Bed\" where Room_Number between 601 and 655"
        q9 = "update room_details set Room_Cost = 2500 where Room_Number between 601 and 655"
        line.execute(q8)
        line.execute(q9)
        con.commit()
    elif l1[i] in icu:
        q10 = "update room_details set Room_Type = \"Intensive Care Unit\" where Room_Number between 501 and 520"
        q11 = "update room_details set Room_Cost = 6000 where Room_Number between 501 and 520"
        line.execute(q10)
        line.execute(q11)
        con.commit()
    elif l1[i] in ot:
        q12 = "update room_details set Room_Type = \"Operation Theatre\" where Room_Number between 521 and 530"
        line.execute(q12)
        con.commit()
line.close()
con.close()'''