import mysql.connector as m
from autogenerate import autogen_docid
def add_doc():
    con = m.connect(host = 'localhost', user = 'root', password = 'mysql', database = 'silverline_hospital')
    line = con.cursor()
    doc_id = autogen_docid()
    doc_nm_inp = input('Doctor\'s Name(format- <firstname> <middlename> <lastname>):\n')
    doc_nm = 'Dr. ' + doc_nm_inp.title()
    sp_inp = input('Speciality:\n')
    sp = sp_inp.capitalize()
    visit = int(input('Enter Visit Charges:\n'))
    query = "insert into doctors values('{}','{}','{}',{})".format(doc_id,doc_nm,sp,visit)
    line.execute(query)
    con.commit()
    print('Doctor added Successfully!\nDoctor ID:  ',doc_id)
    line.close()
    con.close()