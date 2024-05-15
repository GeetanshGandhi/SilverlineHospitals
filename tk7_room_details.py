import mysql.connector as m
from datetime import date
from tkinter import *
from tkinter import font as fs
from PIL import Image,ImageTk

def room_details(dependency):
    con = m.connect(user='root', password='mysql', host='localhost', database='silverline_hospital')
    line = con.cursor()
    #fetching number of rooms
    query = "SELECT * FROM room_details where Availability = 0 and Room_type not like 'Operation Theatre'"
    line.execute(query)
    records = line.fetchall()
    num_private_room_available = 0
    num_shared_room_available = 0
    num_icu_rooms_available = 0
    num_general_ward_beds_available = 0
    
    for record in records:
        if record[1] == "Private Room":
            cost_pvt = record[2]
            num_private_room_available = num_private_room_available + 1
        if record[1] == "Shared Room":
            num_shared_room_available = num_shared_room_available + 1
            cost_shr = record[2]
        if record[1] == "Intensive Care Unit":
            num_icu_rooms_available = num_icu_rooms_available + 1
            cost_icu = record[2]
        if record[1] == "General Ward Bed":
            num_general_ward_beds_available = num_general_ward_beds_available + 1
            cost_gwb = record[2]

    pvtstr = '''1. single bed private room
2. equipped with entertainment amenities
3. 1 person family lounge area
4. prompt medical supervision
- ROOMS AVAILABLE: %d
- COST PER DAY: %d'''%(num_private_room_available,cost_pvt)
    shrstr = '''1. 2 Beds (shared/personal) 
2. equipped with entertainment amenities
3. short visit area (for families)
4. prompt medical supervision
- ROOMS AVAILABLE: %d
- Cost per day: %d'''%(num_shared_room_available,cost_shr)
    gwbstr = '''1. Each bed is highly automatic 
2. beds equipped with easy remote access
3. prompt medical supervision
- BEDS AVAILABLE: %d
- COST PER DAY: %d'''%(num_general_ward_beds_available,cost_gwb)
    icustr = '''1. ICU's are highly equipped rooms\nwith all the possible machinery
2. no family lounge
3. super highly monitered from doctors 
4. permanent nurse present
- ICU'S AVAILABLE: %d
- COST PER DAY: %d'''%(num_icu_rooms_available,cost_icu)
    #creating GUI
    if dependency == 1:
        roomdet = Toplevel()
    elif dependency == 0:
        roomdet = Tk()
    roomdet.geometry('1000x500')
    roomdet.title('Room Details')
    roomdet.resizable(False,False)
    #adding background and logo
    img_open = Image.open("Slide1.jpg")
    resize = img_open.resize((1000,500), Image.ANTIALIAS)
    img_openre = ImageTk.PhotoImage(resize)
    img_open_logo = Image.open("Logo.png")
    resize = img_open_logo.resize((180,80), Image.ANTIALIAS)
    img_openre_logo = ImageTk.PhotoImage(resize)
    #creating canvas
    canva7 = Canvas(roomdet, width = 300, height = 300, highlightthickness = 0)
    canva7.pack(fill = "both", expand = True)
    canva7.create_image(0,0, image = img_openre, anchor = "nw")
    canva7.create_image(0,0, image = img_openre_logo, anchor = "nw")
    #font profile
    titlefont = fs.Font(family="berlin sans fb", size=28)
    headfont = fs.Font(family="algerian", size=20)
    city = fs.Font(family="berlin sans fb", size=15)
    subheadfont = fs.Font(family = 'book antiqua', size=20, weight = 'bold')
    bodyfont = fs.Font(family = 'consolas', size = 13)

    #inserting texts
    canva7.create_text(500, 20, text = 'Silverline Multi-Speciality Hospitals', font = titlefont)
    canva7.create_text(500, 50, text = 'Indore', font = city)
    canva7.create_text(500, 80, text = 'Room Details', font = headfont, fill = 'red')
    canva7.create_text(800, 80, text= 'Date: %s'%str(date.today()), font=bodyfont)

    canva7.create_text(50, 140, text = 'Private Room', font = subheadfont, anchor = 'w')
    canva7.create_text(540, 140, text = 'Shared Room', font = subheadfont, anchor = 'w')
    canva7.create_text(50, 320, text = 'General Ward Bed', font = subheadfont, anchor = 'w')
    canva7.create_text(540, 320, text = 'Intensive Care Unit', font = subheadfont, anchor = 'w')

    canva7.create_text(50, 155, text = pvtstr, font = bodyfont, fill = 'navy', anchor = 'nw')
    canva7.create_text(540, 155, text = shrstr, font = bodyfont, fill = 'navy', anchor = 'nw')
    canva7.create_text(50, 335, text = gwbstr, font = bodyfont, fill = 'navy', anchor = 'nw')
    canva7.create_text(540, 335, text = icustr, font = bodyfont, fill = 'navy', anchor = 'nw')

    #close button
    closebutton = Button(roomdet, text="Close", command=roomdet.destroy, font=bodyfont, bg = "navy", borderwidth = 5,
            fg = "white")
    canva7.create_window(430, 470, window = closebutton)

    #mainloop
    roomdet.mainloop()
