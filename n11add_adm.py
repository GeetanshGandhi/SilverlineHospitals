import mysql.connector as m
from autogenerate import autogen_userid

def add_adm():
    con =  m.connect(host = 'localhost', user = 'root', password = 'mysql', database = 'silverline_hospital')
    line = con.cursor()
    query1 = "select * from login"
    line.execute(query1)
    res = line.fetchall()

    user = autogen_userid()
    adm_nm = input('Administrator\'s Name:  ')
    adm_nm_cap = adm_nm.title()
    pw1 = []
    for i in range(len(res)):
        pw1.append(res[i][1])
    pw2 = input('Enter a unique 4-digit password:  ')
    pw3 = 'silver' + pw2
    #password validation
    while pw3 in pw1 or len(pw2) != 4 or pw2.isdigit() == False:
        pw2 = input('Provided password is already taken or is Invalid(must be unique, numeric and exactly 4-digit). Re-Enter:  ')
        pw3 = 'silver' + pw2

    query2 = "insert into login values('{}','{}','{}')".format(user,pw3,adm_nm_cap)
    print('''Administrator added successfully!
Admin User ID:      %s
Password:           %s'''%(user,pw3))
    line.execute(query2)
    con.commit()
    line.close()
    con.close()