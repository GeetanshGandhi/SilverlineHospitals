from tkinter import *
from tkinter import font as fs
from PIL import Image, ImageTk
from datetime import date

def bank_details(dependency):
    # making tkinter window
    if dependency == 1:
        bdet = Toplevel()
        bdet.geometry("750x400")
        bdet.title("Bank Details")
        bdet.resizable(False,False)
    elif dependency == 0:
        bdet = Tk()
        bdet.geometry("750x400")
        bdet.title("Bank Details")
        bdet.resizable(False,False)
    # adding background image
    img_open = Image.open("Slide1.jpg")
    resize1 = img_open.resize((750, 400), Image.ANTIALIAS)
    img_openre = ImageTk.PhotoImage(resize1)
    # canvas properties
    canva5 = Canvas(bdet, width=750, height=400, bg="blue")
    canva5.pack(fill="both", expand=True)
    canva5.configure(bg="powder blue")
    canva5.create_image(0, 0, image=img_openre, anchor="nw")
    # font profile
    titlefont = fs.Font(family="berlin sans fb", size=32)
    cityfont = fs.Font(family = 'berlin sans fb', size = 14)
    bodyfont = fs.Font(family="ms word", size=16)
    headfont = fs.Font(family="algerian", size=20, weight="bold")
    datefont = fs.Font(family="consolas", size=14, weight="bold")
    # title
    canva5.create_text(375, 25, text="Silverline Multi-Speciality Hospitals", font=titlefont)
    canva5.create_text(375, 60, text="Indore", font=cityfont)
    canva5.create_text(650, 90, text="Date : %s"%date.today(), font=datefont, anchor='center')
    # Header
    canva5.create_text(375, 90, text="Bank Details", font=headfont, fill="red")
    # Name of Bank
    canva5.create_text(335, 135, text="Name of the Bank : ", font=bodyfont)
    canva5.create_text(480, 135, text="State Bank", font=bodyfont, fill="navy blue")
    # Name of Branch
    canva5.create_text(325, 170, text="Name of the Branch : ", font=bodyfont)
    canva5.create_text(480, 170, text="M.G. Road", font=bodyfont, fill="navy blue")
    # Branch Code
    canva5.create_text(325, 205, text="Branch Code No : ", font=bodyfont)
    canva5.create_text(440, 205, text="04241", font=bodyfont, fill="navy blue")
    # Address
    canva5.create_text(170, 240, text="Address : ", font=bodyfont, anchor='w')
    canva5.create_text(440, 240, text="Kothari Market ,Near Rajwada, Indore", font=bodyfont, fill="navy blue")
    # IFSC Code
    canva5.create_text(300, 275, text="IFSC Code : ", font=bodyfont)
    canva5.create_text(420, 275, text=" IDBI00J028", font=bodyfont, fill="navy blue")
    # UPI ID
    canva5.create_text(255, 310, text="UPI ID : ", font=bodyfont)
    canva5.create_text(420, 310, text=" 9526653715@indianbank ", font=bodyfont, fill="navy blue")
    # close button
    button = Button(bdet, text='Close', font = datefont, command=bdet.destroy, borderwidth=5, fg='white', bg='navy')
    canva5.create_window(375,340, window=button, anchor='n')
    # mainloop
    bdet.mainloop()
