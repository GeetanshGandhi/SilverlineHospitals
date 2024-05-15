from tkinter import *
from tkinter import font as fs
from PIL import Image, ImageTk

def patient_details(pid, pname, adhar, phnno, tid, trtname, ins, date_adm, doc, rno, bid):
    #values are coming through arguements
    #defining GUI and adding background:
    card = Tk()
    card.geometry("700x550")
    card.title("Out Patient Department")
    card.resizable(False,False)
    img_open = Image.open("Slide1.jpg") #background image configuration
    resize1 = img_open.resize((700,550), Image.ANTIALIAS)
    img_openre = ImageTk.PhotoImage(resize1)
    canva1 = Canvas(card, width = 700, height = 550, highlightthickness = 0)
    canva1.pack(fill = "both", expand = True)
    canva1.configure(bg = "powder blue")
    canva1.create_image(0,0, image = img_openre, anchor = "nw") #canvas setup
    #font profile
    titlefont = fs.Font(family="berlin sans fb", size=32)
    headfont = fs.Font(family="algerian", size=15)
    city = fs.Font(family="berlin sans fb", size=15)
    bodyfont = fs.Font(family="monaco", size=16)
    pidfont = fs.Font(family="Copperplate Gothic Bold", size=21)
    messagefont = fs.Font(family="Forte", size=18)
    button_font = fs.Font(family="Arial", size=15)
    namefont = fs.Font(family="Wide latin", size=13)
    authfont = fs.Font(family="consolas", size=15)
    pnamefont = fs.Font(family = 'monaco', size = 12)
    #text object insertion
    canva1.create_text(350, 25, text="Silverline Multi-Speciality Hospitals", font=titlefont)
    canva1.create_text(350, 60, text="INDORE", font=city)
    canva1.create_text(350, 100, text="Patient Details", font=headfont, fill="red")
    canva1.create_text(350, 115, text="Patient ID : %s"%pid, font=pidfont, anchor="n")
    canva1.create_text(30, 175, text="Patient Name", font=bodyfont, anchor="w")
    canva1.create_text(370, 175, text=pname, font=pnamefont, anchor="w", fill = "blue")
    canva1.create_text(30, 200, text="AadharCard Number", font=bodyfont, anchor="w")
    canva1.create_text(370, 200, text=adhar, font=bodyfont, anchor="w", fill = "blue")
    canva1.create_text(30, 225, text="Contact(Guadian)", font=bodyfont, anchor="w")
    canva1.create_text(370, 225, text=phnno, font=bodyfont, anchor="w", fill = "blue")
    canva1.create_text(30, 250, text="Treatment ID", font=bodyfont, anchor="w")
    canva1.create_text(370, 250, text=tid, font=bodyfont, anchor="w", fill = "blue")
    canva1.create_text(30, 275, text="Treatment Undergoing", font=bodyfont, anchor="w")
    canva1.create_text(370, 275, text=trtname, font=bodyfont, anchor="w", fill = "blue")
    canva1.create_text(30, 300, text="Insurance Number", font=bodyfont, anchor="w")
    if ins is None: #display appropriate msg if no insurance
        canva1.create_text(370, 300, text="Not Insured", font=bodyfont, anchor="w", fill="blue")
    else:
        canva1.create_text(370, 300, text=ins, font=bodyfont, anchor="w", fill = "blue")
    canva1.create_text(30, 325, text="Admission Date", font=bodyfont, anchor="w")
    canva1.create_text(370, 325, text=date_adm, font=bodyfont, anchor="w", fill = "blue")
    canva1.create_text(30, 350, text="Doctor-in-Charge", font=bodyfont, anchor="w")
    canva1.create_text(370, 350, text=doc, font=bodyfont, anchor="w", fill = "blue")
    canva1.create_text(30, 375, text="Room Number", font=bodyfont, anchor="w")
    canva1.create_text(370, 375, text=rno, font=bodyfont, anchor="w", fill = "blue")
    canva1.create_text(30, 400, text="Bill Number", font=bodyfont, anchor="w")
    canva1.create_text(370, 400, text=bid, font=bodyfont, anchor="w", fill = "blue")
    canva1.create_text(20, 430, text="Wishing the patient a speedy recovery!", font=messagefont, anchor="w")
    canva1.create_text(680, 510, text="Silverline Hospitals", font=namefont, anchor="e")
    canva1.create_text(680, 490, text="Authoried By", font=authfont, anchor="e")
    #close button
    b1 = Button(card, text="Close", command=card.destroy, font=button_font, bg = "navy", borderwidth = 5,
            fg = "white")
    canva1.create_window(50, 500, window = b1)
    card.mainloop() #mainloop declaration