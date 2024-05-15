from tkinter import *
from tkinter import font as fs
from PIL import Image, ImageTk
import mysql.connector as m
from tk5_bank_details import bank_details
from id_validations import bid_valid
from n3days_per_room import days_per_room
from n7bill_graph import pie_chart

def billdisplay(b_id_input=None):
    # fetching data
    if b_id_input is None:
        b_id_inp = input('Enter Bill Number\n')
        b_id_input = bid_valid(b_id_inp)
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor()
    try:
        query1 = "select * from bill_details where Bill_Number " \
                 "= '{}'".format(b_id_input)
        line.execute(query1)
        res1 = line.fetchone()
    except:
        print('No such record found! Please try again or Contact admin for any issue.')
        return 0
    p_id_input = res1[1]
    p_name = res1[2]
    t_name = res1[3]
    t_id = res1[4]
    doc_id = res1[5]
    reg_fees = float(res1[6])
    trtcost = float(res1[7])
    service = float(res1[9])
    visit = float(res1[10])
    surgery_charges = float(res1[11])
    cost_wo_tax = float(res1[13])
    tax = (res1[14]) / 2
    cost_w_tax = res1[15]
    roundfig = int(cost_w_tax)
    pmethod = res1[16]
    status_bool = res1[17]
    status = 'Stand-by'
    if status_bool == 0:
        status = 'Due'
    elif status_bool == 1:
        status = 'Paid'
    note = 'This is an electronic generated bill\nFor any queries, contact Admin.' \
           '\nContact admin to procure CSV for bill.'
    query2 = "select Doctor_Name, Date_Admission, Date_Discharge from discharged_patients " \
             "where Patient_Id = '{}'".format(p_id_input)
    line.execute(query2)
    res2 = line.fetchone()
    doc_name = res2[0]
    dateadm = res2[1]
    datedisch = res2[2]
    roomdict = list(days_per_room(1, p_id_in=p_id_input))[6]
    total_days = list(days_per_room(1, p_id_in=p_id_input))[5]
    visitperday = visit / total_days
    serviceperday = service / total_days

    # making GUI  and configuring for fullscreen
    bill = Tk()
    bill.configure(bg="powder blue")
    bill.attributes('-fullscreen', True)
    w = bill.winfo_screenwidth()  # system's screen's width
    h = bill.winfo_screenheight()  # system's scrnee's height
    xs = w / 1366
    ys = h / 768
    # adding background and logo
    img_open1 = Image.open("Slide1.jpg")
    resize1 = img_open1.resize((w, h), Image.ANTIALIAS)
    img_re1 = ImageTk.PhotoImage(resize1)
    img_open2 = Image.open("Logo.png")
    resize2 = img_open2.resize((int(220 * xs), int(120 * ys)), Image.ANTIALIAS)
    img_re2 = ImageTk.PhotoImage(resize2)
    # creating canvas
    canva4 = Canvas(bill, highlightthickness=0)
    canva4.pack(fill='both', expand=True)
    canva4.configure(bg='red')
    canva4.create_image(0, 0, image=img_re1, anchor='nw')
    canva4.create_image(0, 0, image=img_re2, anchor='nw')
    # font profile
    headfont = fs.Font(family="berlin sans fb", size=int(40 * ys))
    city = fs.Font(family='berlin sans fb', size=int(20 * ys))
    subjectfont = fs.Font(family='algerian', size=int(30 * ys))
    infofont = fs.Font(family='consolas', size=int(15 * ys))
    sp_colhead_font = fs.Font(family='consolas', size=int(20 * ys), weight='bold')
    subheadfont = fs.Font(family='algerian', size=int(20 * ys), weight='bold')
    bodyfont = fs.Font(family='ar essence', size=int(18 * ys))
    subbodyfont = fs.Font(family='consolas', size=int(14 * ys))
    valuefont = fs.Font(family='consolas', size=int(15 * ys))
    totalbodyfont = fs.Font(family='ar essence', size=int(20 * ys))
    totalvaluesfont = fs.Font(family='consolas', size=int(20 * ys))
    datefont = fs.Font(family='consolas', size=int(12 * ys), weight='bold')
    # adding texts
    canva4.create_text((w / 2) * xs, 35 * ys, text="Silverline Multi Speciality Hospital", anchor='center',
                       font=headfont)
    canva4.create_text((w / 2) * xs, 75 * ys, text='Indore', font=city, anchor='center')
    canva4.create_text((w / 2) * xs, 120 * ys, text="Bill Details", font=subjectfont, anchor='center', fill='red')

    canva4.create_text(1320 * xs, 50 * ys, text='Date of Admission:', font=datefont, anchor='e')
    canva4.create_text(1320 * xs, 70 * ys, text=dateadm, font=datefont, anchor='e', fill='navy blue')
    canva4.create_text(1320 * xs, 90 * ys, text='Date of Discharge:', font=datefont, anchor='e')
    canva4.create_text(1320 * xs, 110 * ys, text=datedisch, font=datefont, anchor='e', fill='navy blue')
    canva4.create_text(35 * xs, 140 * ys, text='Patient ID:  %s' % p_id_input, font=infofont, anchor='w')
    canva4.create_text(1320 * xs, 140 * ys, text='Bill Number:  %s' % b_id_input, font=infofont, anchor='e')
    canva4.create_text(35 * xs, 160 * ys, text='Patient Name:  %s' % p_name, font=infofont, anchor='w')
    canva4.create_text(1320 * xs, 160 * ys, text='Treatment ID: %s' % t_id, font=infofont, anchor='e')
    canva4.create_text(1320 * xs, 181 * ys, text='Treatment:  %s' % t_name, font=infofont, anchor='e')
    canva4.create_text(35 * xs, 181 * ys, text='Doctor:  %s' % doc_name, font=infofont, anchor='w')

    canva4.create_text((w / 2) * xs, 185 * ys, text='TAX INVOICE', font=subheadfont, anchor='center')
    canva4.create_text(69 * xs, 230 * ys, text='S.No.', font=sp_colhead_font, anchor='center')
    canva4.create_text(69 * xs, 280 * ys, text='1', font=sp_colhead_font, anchor='center')
    canva4.create_text(69 * xs, 310 * ys, text='2', font=sp_colhead_font, anchor='center')
    canva4.create_text(69 * xs, 340 * ys, text='3', font=sp_colhead_font, anchor='center')
    canva4.create_text(69 * xs, 370 * ys, text='4', font=sp_colhead_font, anchor='center')
    canva4.create_text(69 * xs, 400 * ys, text='5', font=sp_colhead_font, anchor='center')

    canva4.create_text(400 * xs, 230 * ys, text='Particulars', font=sp_colhead_font, anchor='center')
    canva4.create_text(140 * xs, 280 * ys, text='Registeration Fees', font=bodyfont, anchor='w')
    canva4.create_text(140 * xs, 310 * ys, text='Treatment Cost (One-Time + Daily)', font=bodyfont, anchor='w')
    canva4.create_text(140 * xs, 340 * ys, text='Service Charges', font=bodyfont, anchor='w')
    canva4.create_text(140 * xs, 370 * ys, text='Doctor\'s Visit Charges', font=bodyfont, anchor='w')
    canva4.create_text(140 * xs, 400 * ys, text='Room Cost', font=bodyfont, anchor='w')

    canva4.create_text(800 * xs, 230 * ys, text='Rate', font=sp_colhead_font, anchor='e')
    canva4.create_text(800 * xs, 280 * ys, text=reg_fees, font=valuefont, anchor='e')
    canva4.create_text(800 * xs, 310 * ys, text=trtcost, font=valuefont, anchor='e')
    canva4.create_text(800 * xs, 340 * ys, text=serviceperday, font=valuefont, anchor='e')
    canva4.create_text(800 * xs, 370 * ys, text=visitperday, font=valuefont, anchor='e')

    canva4.create_text(1000 * xs, 230 * ys, text='Quantity', font=sp_colhead_font, anchor='center')
    canva4.create_text(1000 * xs, 280 * ys, text=1, font=valuefont, anchor='center')
    canva4.create_text(1000 * xs, 310 * ys, text=1, font=valuefont, anchor='center')
    canva4.create_text(1000 * xs, 340 * ys, text=total_days, font=valuefont, anchor='center')
    canva4.create_text(1000 * xs, 370 * ys, text=total_days, font=valuefont, anchor='center')

    canva4.create_text(1225 * xs, 230 * ys, text='Amount', font=sp_colhead_font, anchor='center')
    canva4.create_text(1275 * xs, 280 * ys, text=reg_fees, font=valuefont, anchor='e')
    canva4.create_text(1275 * xs, 310 * ys, text=trtcost, font=valuefont, anchor='e')
    canva4.create_text(1275 * xs, 340 * ys, text=service, font=valuefont, anchor='e')
    canva4.create_text(1275 * xs, 370 * ys, text=visit, font=valuefont, anchor='e')
    # adding specific room charges
    names = list(roomdict.keys())
    val = list(roomdict.values())
    ycoor = 400
    num = 1
    for i in range(len(roomdict)):
        if roomdict[names[i]][0] != 0:
            canva4.create_text(350 * xs, ycoor * ys, text=str(num) + ') ' + str(names[i]), font=subbodyfont, anchor='w')
            canva4.create_text(800 * xs, ycoor * ys, text=float(val[i][1]), font=valuefont, anchor='e')
            canva4.create_text(1000 * xs, ycoor * ys, text=val[i][0], font=valuefont, anchor='center')
            canva4.create_text(1275 * xs, ycoor * ys, text=float(val[i][2]), font=valuefont, anchor='e')
            ycoor += 28
            num += 1
    # surgery charges, if any
    if surgery_charges != 0:
        canva4.create_text(69 * xs, 485 * ys, text='6', font=sp_colhead_font, anchor='center')
        canva4.create_text(140 * xs, 485 * ys, text='Surgery Charges', font=bodyfont, anchor='w')
        canva4.create_text(800 * xs, 485 * ys, text=surgery_charges, font=valuefont, anchor='e')
        canva4.create_text(1000 * xs, 485 * ys, text=1, font=valuefont, anchor='center')
        canva4.create_text(1275 * xs, 485 * ys, text=surgery_charges, font=valuefont, anchor='e')

    canva4.create_text(1100 * xs, 535 * ys, text='Total: ', font=totalbodyfont, anchor='e')
    canva4.create_text(1100 * xs, 565 * ys, text='CGST@9%: ', font=totalbodyfont, anchor='e')
    canva4.create_text(1100 * xs, 595 * ys, text='SGST@9% ', font=totalbodyfont, anchor='e')
    canva4.create_text(1100 * xs, 625 * ys, text='Grand Total: ', font=totalbodyfont, anchor='e')
    canva4.create_text(1100 * xs, 680 * ys, text='Payable Amount: ', font=totalbodyfont, anchor='e')

    canva4.create_text(1275 * xs, 535 * ys, text=cost_wo_tax, font=totalvaluesfont, anchor='e', fill='navy blue')
    canva4.create_text(1275 * xs, 565 * ys, text=tax, font=totalvaluesfont, anchor='e', fill='navy blue')
    canva4.create_text(1275 * xs, 595 * ys, text=tax, font=totalvaluesfont, anchor='e', fill='navy blue')
    canva4.create_text(1275 * xs, 626 * ys, text=cost_w_tax, font=totalvaluesfont, anchor='e', fill='navy blue')
    canva4.create_text(1275 * xs, 680 * ys, text=str(roundfig), font=totalvaluesfont, anchor='e', fill='navy blue')

    canva4.create_text(69 * xs, 550 * ys, text='Payment Method:', font=totalbodyfont, anchor='w')
    canva4.create_text(400 * xs, 550 * ys, text=pmethod, font=totalvaluesfont, fill='navy blue', anchor='w')
    canva4.create_text(69 * xs, 590 * ys, text='Status:', font=totalbodyfont, anchor='w')
    canva4.create_text(400 * xs, 590 * ys, text=status, font=totalvaluesfont, fill='navy blue', anchor='w')
    canva4.create_text(69 * xs, 650 * ys, text=note, font=infofont, anchor='w')

    # buttons to view bank details and pie-chart summary
    button1 = Button(bill, text='Click to view Bank Details', font=infofont, command=lambda: [bank_details(1)],
                     borderwidth=5, fg='white', bg='navy')
    canva4.create_window(583 * xs, 710 * ys, window=button1, anchor='ne')
    button2 = Button(bill, text='OK', font=infofont, command=bill.destroy, borderwidth=5,
                     fg='white', bg='navy')
    canva4.create_window((1366 / 2) * xs, 710 * ys, window=button2, anchor='n')
    button3 = Button(bill, text='Click to view pie-chart summary for bill', font=infofont,
                     command=lambda: [pie_chart(b_id_input)], borderwidth=5, fg='white', bg='navy')
    canva4.create_window(783 * xs, 710 * ys, window=button3, anchor='nw')
    # mainloop
    bill.mainloop()

billdisplay("1BD0007")
