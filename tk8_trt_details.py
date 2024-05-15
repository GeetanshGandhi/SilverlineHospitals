from tkinter import *
from tkinter import font as fs
from PIL import Image,ImageTk
from datetime import date
from list_dict import treatments

def trt_det(dependency):
    #making GUI
    if dependency == 1:
        trtdets = Toplevel()
    else:
        trtdets = Tk()
    trtdets.geometry("1000x550")
    trtdets.configure(bg="red")
    trtdets.title("Out Patient Department")
    trtdets.resizable(False,False)
    #adding background and logo
    img_open = Image.open("Slide1.jpg")
    resize1 = img_open.resize((1000,550), Image.ANTIALIAS)
    img_openre = ImageTk.PhotoImage(resize1)
    img_open_logo = Image.open("logo.png")
    resize1 = img_open_logo.resize((210,100), Image.ANTIALIAS)
    img_openre_logo = ImageTk.PhotoImage(resize1)
    #creating canvas
    canva8 = Canvas(trtdets, width = 1000, height = 550, highlightthickness = 0)
    canva8.pack(fill = "both", expand = True)
    canva8.configure(bg = "powder blue")
    canva8.create_image(0,0, image = img_openre, anchor = "nw")
    canva8.create_image(0,0, image = img_openre_logo, anchor = 'nw')
    #font profile
    titlefont = fs.Font(family="berlin sans fb", size=25)
    headfont = fs.Font(family="algerian", size=20)
    city = fs.Font(family="berlin sans fb", size=14)
    subheadfont = fs.Font(family = 'Arial', size = 17)
    bodyfont = fs.Font(family = 'consolas', size = 14)
    buttonfont = fs.Font(family = 'consolas', size = 13, weight = 'bold')
    #creating text
    canva8.create_text(500, 20, text = 'Silverline Multi-Speciality Hospitals', font = titlefont)
    canva8.create_text(500, 50, text = 'Indore', font = city)
    canva8.create_text(500, 80, text = 'Treatments Available', font = headfont, fill = 'red')
    canva8.create_text(875, 80, text='Date: %s'%str(date.today()), font=bodyfont)
    #fetching data from list_dict.py to display
    ycoor1 = 120
    keys = list(treatments.keys())
    vals = list(treatments.values())
    for i in range(len(treatments)):
        canva8.create_text(50, ycoor1, text = keys[i]+':', font = subheadfont, anchor = 'w')
        temp = ''
        for j in range(len(vals[i])):
            temp += vals[i][j]+'\t'
        canva8.create_text(200, ycoor1, text = temp, font = bodyfont, anchor = 'w', fill = 'navy')
        ycoor1 += 30

    #close button
    closebutton = Button(trtdets, text="Close", command=trtdets.destroy, font=buttonfont, bg = "navy", borderwidth = 5,
            fg = "white")
    canva8.create_window(470, 520, window = closebutton)

    trtdets.mainloop() #mainloop