import mysql.connector as m
con = m.connect(host = 'localhost', user = 'root', password = 'mysql', database = 'silverline_hospital')
line = con.cursor()
query1 = "select * from treatment"
line.execute(query1)
res = line.fetchall()
treatments = {}
id_generation = {}
tname_gen = {}
for i in range(len(res)):
    id_generation[res[i][1]] = [res[i][0],res[i][3],res[i][4]]
    tname_gen[res[i][0]] = res[i][1]

query2 = "select DISTINCT(Category) from treatment"
line.execute(query2)
res1 = line.fetchall()
for i in range(len(res1)):
    query2 = "select Category,Treatment_Name from treatment where Category = '{}'".format(res1[i][0])
    line.execute(query2)
    res2 = line.fetchall()
    temp = []
    for i in range(len(res2)):
        temp.append(res2[i][1])
    treatments[res2[0][0]] = temp

query9 = "select * from doctors"
line.execute(query9)
res9 = line.fetchall()
doctors = {}
for i in range(len(res9)):
    doctors[res9[i][0]] = [res9[i][1],res9[i][2],res9[i][3]]
'''
import mysql.connector as m
con = m.connect(host = 'localhost', user = 'root', password = 'mysql', database = 'silverline_hospital')
line = con .cursor()

treatments = {'Cardio' : ['Bypass Surgery','Valve SUrgery','Heart ATtack'],
'Lungs' : ['Asthma','Tuberculosis','Pneumonia','Covid-19'],
'Neuro':['Brain Tumour Surgery','Stroke','Seizure'],
'ENT':['Ear Discharge','Tonsils','DNS'],
'Ortho':['Joint Replacement','Fracture'],
'General':['Abdominal Surgery','Laproscopy'],
'Plastic':['Burn Surgery','Cosmetic Surgery'],
'Eye':['Lasik Curation Surgery','Apex Retina']}

id_generation = {'Bypass Surgery':['Car001','D001',130000,1,3],
                 'Valve Surgery':['Car002', 'D001',50000,1,3],
                 'Heart Attack':['Car003','D001',10000,0,0],
                 'Asthma' : ['Lun001','D002',4000,0,0],
                 'Tuberculosis' : ['Lun002','D002',2500,0,0],
                 'Pneumonia': ['Lun003','D002',8000,0,0],
                 'Covid-19' : ['Lun004', 'D002',20000,0,0],
                 'Brain Tumour Surgery' : ['Neu001','D003',150000,1,3],
                 'Stroke': ['Neu002','D003',50000,1,3],
                 'Seizure' : ['Neu003','D003',10000,0,0],
                 'Ear Discharge' : ['Ent001','D004',8000,0,0],
                 'Tonsils' : ['Ent002','D004',20000,1,1],
                 'DNS' : ['Ent003','D004',15000,1,1],
                 'Joint Replacement':['Ort001','D005',100000,1,3],
                 'Fracture':['Ort002','D005',50000,1,2],
                 'Burn Surgery':['Pla001','D007',60000,1,3],
                 'Cosmetic Surgery':['Pla002','D007',100000,1,2],
                 'Abdominal Surgery':['Gen001','D008',80000,1,3],
                 'Laproscopy':['Gen002','D008',75000,1,3],
                 'Lasik Curation Surgery':['Eye001','D009',55000,1,2.5],
                 'Apex Retina':['Eye002','D009',175000,1,2]}
tname_gen = {'Car001' : 'Bypass Surgery',
             'Car002' : 'Valve Surgery',
             'Car003' : 'Heart Attack',
             'Lun001' : 'Asthma',
             'Lun002' : 'Tuberculosis',
             'Lun003' : 'Pneumonia',
             'Lun004' : 'Covid-19',
             'Neu001' : 'Brain Tumour',
             'Neu002' : 'Stroke',
             'Neu003' : 'Seizure',
             'Ent001' : 'Ear Discharge',
             'Ent002' : 'Tonsils',
             'Ent003' : 'DNS',
             'Ort001' : 'Joint Replacement',
             'Ort002' : 'Fracture',
             'Pla001' : 'Cosmetic Surgery',
             'Pla002' : 'Burn Surgery',
             'Gen001' : 'Abdominal Surgery',
             'Gen002' : 'Laproscopy',
             'Eye001' : 'Lasik Curation Surgery',
             'Eye002' : 'Apex Retina'}

doctors = {'D001':['Dr. Bharat Rawat',"Cardiologist",2000],
           'D002':['Dr. Ravi Doshi','Pulmonologist',2000],
           'D003':['Dr. Nilesh Jain','Neurologist',2200],
           'D004':['Dr. Gunwant Yashla','ENT Specialist',1500],
           'D005':['Dr. Vikas Jain','Orthopedist',1700],
           'D006':['Dr. Dolly Mehra','General Physician',2000],
           'D007':['Dr. Vishal Jain','General Surgeon',1500],
           'D008':['Dr. Nishant Khare','Plastic Surgeon',1600],
           'D009':['Dr. GVN Ramkumar','Eye Surgeon',1500]}
list1 = list(id_generation.keys())
list2 = list(id_generation.values())
for i in range(len(id_generation)):
    q1 = "insert into treatment(Treatment_Id, Treatment_Name, Doctor_Id,Treatment_Cost, Surgery_Required, Surgery_Time_hrs)" \
    "values('{}','{}','{}',{},{},{})".format(list2[i][0],list1[i],list2[i][1],list2[i][2],list2[i][3],list2[i][4])
    line.execute(q1)
    con.commit()
q2 = "update treatment set Category = \"Cardio\" where Treatment_Id like 'Car%'"
q3 = "update treatment set Category = \"ENT\" where Treatment_Id like 'Ent%'"
q4 = "update treatment set Category = \"Neuro\" where Treatment_Id like 'Neu%'"
q5 = "update treatment set Category = \"Lungs\" where Treatment_Id like 'Lun%'"
q6 = "update treatment set Category = \"Ortho\" where Treatment_Id like 'Ort%'"
q7 = "update treatment set Category = \"General\" where Treatment_Id like 'Gen%'"
q8 = "update treatment set Category = \"Plastic\" where Treatment_Id like 'Pla%'"
q9 = "update treatment set Category = \"Eye\" where Treatment_Id like 'Eye%'"
line.execute(q2)
line.execute(q3)
line.execute(q4)
line.execute(q5)
line.execute(q6)
line.execute(q7)
line.execute(q8)
line.execute(q9)

list3 = list(doctors.keys())
list4 = list(doctors.values())
for j in range(len(doctors)):
    q7 = "insert into doctors values('{}','{}','{}',{})".format(list3[j],list4[j][0],list4[j][1],list4[j][2])
    line.execute(q7)
    con.commit()

con.commit()'''