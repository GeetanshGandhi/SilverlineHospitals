import matplotlib.pyplot as p
import mysql.connector as m

def pie_chart(bill_num):
	con = m.connect(user='root', password='mysql', host='localhost', database='silverline_hospital')
	line = con.cursor()
	query = "select Registeration_Fees, Treatment_Cost,Room_Cost,Service_Charges,Tax from bill_details where Bill_Number='{}'".format(bill_num)
	line.execute(query)
	d = line.fetchone()

	fig = p.figure()
	fig.patch.set_facecolor('cyan')

	p.pie([d[0], d[1], d[2], d[3], d[4]],
	      labels=["Registration fees", "Treatment Cost", "Room Cost",
	          "Service Charges", "Tax"
	      ],shadow=True, autopct='%1.1f%%')

	p.title("BILL SUMMARY")
	p.show()

	line.close()
	con.close()