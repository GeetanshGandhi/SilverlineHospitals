from tkinter import *
from tkinter import font as fs
from PIL import Image, ImageTk
import mysql.connector as m
from list_dict import *
from roomno import roomdetails
from tk8_trt_details import trt_det
from tk7_room_details import room_details

data_tuple = ()
def adm_form(error = 0):
    global data_tuple

    try:
        def admission_validation(): #to validate login
            con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
            line = con.cursor()
            global data_tuple #to get data to n1

            name, adhar, mob = nameinp.get(),adharinp.get(),mobinp.get()
            trtnm, room_cat = trtinp.get(),roominp.get()

            insstatus,insnum = insinp.get(), insnuminp.get()
            if len(name) > 50: #restricting name to first 50 characters
                name = name[0:49]
            data_tuple = (name, adhar, mob, trtnm, room_cat, insstatus, insnum)
            query = "select * from room_details where Room_Type = '{}' and Availability = 0".format(room_cat)
            line.execute(query)
            res = line.fetchall()
            #checking various credentials and recursing GUI with appropriate message
            if len(adhar)!=12 or not adhar.isdigit():
                form.destroy()
                adm_form(error = 1)
            elif len(mob)!=10 or mob.isdigit()==False:
                form.destroy()
                adm_form(error = 2)
            elif insstatus == 'Yes' and (insnum is None or insnum.isspace() or insnum == ''
            or insnum[0:2].isalpha()==False or insnum[2:8].isdigit() == False or insnum[-1].isalpha()==False):
                form.destroy()
                adm_form(error = 3)
            elif insstatus == 'Insurance Status':
                form.destroy()
                adm_form(error = 4)
            elif res == ([],):
                form.destroy()
                adm_form(error = 5)
            elif room_cat == 'Select a Room Type':
                form.destroy()
                adm_form(error = 6)
            elif trtnm == 'Select a Treatment':
                form.destroy()
                adm_form(error = 7)
            else:
                form.destroy()

        #making GUI and adding background and logo
        form = Tk()
        # form.protocol()
        form.geometry('1200x650')
        form.title('Patient Admission Form')
        form.resizable(False, False)
        img_open = Image.open("Slide1.jpg")
        resize1 = img_open.resize((1200, 650), Image.ANTIALIAS)
        img_openre = ImageTk.PhotoImage(resize1)    #make it feasible to use in tkinter
        canva6 = Canvas(form, width=1200, height=550, highlightthickness=0)
        canva6.pack(fill="both", expand=True)
        canva6.create_image(0, 0, image=img_openre, anchor="nw")
        img_open_logo = Image.open("Logo.png")
        resize = img_open_logo.resize((180,120), Image.ANTIALIAS)
        img_openre_logo = ImageTk.PhotoImage(resize)
        canva6.create_image(0,0, image = img_openre_logo,anchor = 'nw')
        # font profile
        titlefont = fs.Font(family="berlin sans fb", size=32)
        headfont = fs.Font(family="algerian", size=25)
        city = fs.Font(family="berlin sans fb", size=15)
        bodyfont = fs.Font(family='Consolas', size=20)
        val_alphafont = fs.Font(family='Arial', size=17)
        val_numfont = fs.Font(family='consolas', size=17)
        cdfont = fs.Font(family='Arial', size=16, slant='italic')
        buttonfont = fs.Font(family='Consolas', size=13, weight='bold')
        errorfont = fs.Font(family = 'Franklin Gothic Demi Cond', size = 14)

        #variables to be used
        name, adhar, mob, trtnm = StringVar(), StringVar(), StringVar(), StringVar()
        #creating text objects
        canva6.create_text(600, 25, text="Silverline Multi-Speciality Hospitals", font=titlefont)
        canva6.create_text(600, 60, text="INDORE", font=city)
        canva6.create_text(600, 100, text="Admission Details", font=headfont, fill="red")

        canva6.create_text(95, 175, text="Patient\'s Name:", font=bodyfont, anchor='w')
        canva6.create_text(95, 200, text="Name will be reduced to first 50 characters", font=errorfont, anchor='w')
        canva6.create_text(95, 235, text="Patient\'s Aadhar Number:", font=bodyfont, anchor='w')
        canva6.create_text(95, 295, text="Guardian\'s Contact Number:", font=bodyfont, anchor='w')
        canva6.create_text(820, 295, text="+91", font=cdfont, anchor='w', fill='navy')
        nameinp = Entry(form, width=60, textvariable=name, font=val_alphafont,   justify='center', bg="lemon chiffon",
                        fg='navy')
        canva6.create_window(1100, 175, window=nameinp, anchor="e")
        adharinp = Entry(form, width=12, textvariable=adhar, font=val_numfont, bg="lemon chiffon", fg='navy')
        canva6.create_window(1000, 235, window=adharinp, anchor="e")
        mobinp = Entry(form, width=10, textvariable=mob, font=val_numfont, bg="lemon chiffon", fg='navy')
        canva6.create_window(1000, 295, window=mobinp, anchor="e")
        #treatment input
        trtbut = Button(form, text='Click Here to View Available Treatments', command=lambda: trt_det(1),
                        font=buttonfont,bg='navy', fg='white', borderwidth=4)
        canva6.create_window(300, 350, window=trtbut)
        trtinp = StringVar()
        trtinp.set("Select a Treatment")
        trtopt = OptionMenu(form, trtinp, *id_generation.keys())
        trtopt.configure(bg='lemon chiffon', fg='navy', font=val_alphafont)
        canva6.create_window(900, 350, window=trtopt)
        #room input
        roombut = Button(form, text='Click Here to Know About Rooms', command=lambda: room_details(1), font=buttonfont,
                         bg='navy', fg='white', borderwidth=4)
        canva6.create_window(300, 400, window=roombut)
        roominp = StringVar()
        roominp.set("Select a Room Type")
        room_ch = list(roomdetails.keys())
        room_ch.remove("Operation Theatre") #remove operation theatre from choices
        roomopt = OptionMenu(form, roominp, *room_ch)
        roomopt.configure(bg='lemon chiffon', fg='navy', font=val_alphafont)
        canva6.create_window(900, 400, window=roomopt)
        #insurance input
        insinp = StringVar()
        insinp.set("Insurance Status")
        insopt = OptionMenu(form, insinp, *['Yes','No'])
        insopt.configure(bg = 'lemon chiffon', fg = 'navy', font = val_alphafont)
        canva6.create_window(300, 460, window = insopt)
        insnuminp = StringVar()
        insnuminp = Entry(form, textvariable = insnuminp, width = 9, fg = 'navy', bg= 'lemon chiffon', font = val_numfont)
        canva6.create_text(300, 520, text = 'Enter Insurance Number', font = bodyfont)
        canva6.create_window(900, 520, window = insnuminp)
        admitbutton = Button(form, text = 'Proceed', command = lambda:[admission_validation()], font = buttonfont, fg = 'white', bg = 'navy', borderwidth = 4)
        canva6.create_window(600, 630, window = admitbutton)
        #function to retain previous values
        def insertion_when_restart():
            nameinp.insert(0,data_tuple[0])
            adharinp.insert(0,data_tuple[1])
            mobinp.insert(0,data_tuple[2])
            trtinp.set(data_tuple[3])
            roominp.set(data_tuple[4])
            insinp.set(data_tuple[5])
            insnuminp.insert(0,data_tuple[6])
        #error profile
        if error == 1:
            adhar_err = 'Invalid Aadhar Card Number!\n(Mandatory entry, Must be numeric and 12-digit)'
            canva6.create_text(470,250, text = adhar_err, font = errorfont, fill = 'red', anchor = 'w')
            insertion_when_restart()
        elif error == 2:
            mob_err = 'Invalid Mobile Number!\n(Mandatory, must be numeric and 10-digit)'
            canva6.create_text(500,295, text = mob_err, font = errorfont, fill = 'red', anchor = 'w')
            insertion_when_restart()
        elif error == 3:
            ins_err = 'Invalid Insurance detail!\n(Mandatory if insurance is selected \'Yes\''\
                    '\nMust have 2 letters at beginning, one at the end and 6 digits in between)'
            canva6.create_text(800,450, text = ins_err, font = errorfont, fill = 'red')
            insertion_when_restart()
        elif error == 4:
            ins_err = 'Please select an Insurance Status'
            canva6.create_text(800,450, text = ins_err, font = errorfont, fill = 'red')
            insertion_when_restart()
        elif error == 5:
            room_err = 'This Room type is currently unavailable!\nPlease select some other type.'
            canva6.create_text(500,400, text = room_err, font = errorfont, fill = 'red', anchor = 'w')
            insertion_when_restart()
        elif error == 6:
            room_err = 'Please Select a room!'
            canva6.create_text(500,400, text = room_err, font = errorfont, fill = 'red', anchor = 'w')
            insertion_when_restart()
        elif error == 7:
            trt_err = 'Please select a Treatment!'
            canva6.create_text(500,350, text = trt_err, font = errorfont, anchor ='w', fill = 'red')
            insertion_when_restart()
        form.mainloop()
        return data_tuple
    except NameError:
        data_tuple = tuple()
        return data_tuple