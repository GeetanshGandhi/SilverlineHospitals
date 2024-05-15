from tkinter import *
from tkinter import font as fs
from PIL import Image, ImageTk
'''
p_id = '1AD0001'        #example values
pr = 12
sr = 13
gb = 21
icu = 7
'''
def days_per_room_display(p_id, pr,sr,gwb,icu):
    dprd = Tk()
    dprd.geometry('350x255')
    dprd.configure(bg = "powder blue")
    dprd.title("Days Per Room")
    dprd.resizable(False,False)
    img_open = Image.open("Slide1.jpg")
    resize = img_open.resize((350,255), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(resize)

    canva3 = Canvas(dprd, width = 350, height = 255, highlightthickness = 0)
    canva3.pack(fill = 'both', expand = True)
    canva3.configure(bg = 'powder blue')
    canva3.create_image(0,0,image = img_tk, anchor = 'nw')

    headfont = fs.Font(family = "berlin sans fb", size = 23)
    keyfont = fs.Font(family = 'Segoe Print', size = 16, weight = 'bold')
    valuefont = fs.Font(family='monaco', size=16, weight='bold')
    buttonfont = fs.Font(family = "Arial", size = 14)

    canva3.create_text(165, 10, text = "Patient ID", font = headfont, anchor = 'ne')
    canva3.create_text(185, 10, text = p_id, font = headfont, anchor = 'nw')
    canva3.create_text(175, 10, text = ":", font = headfont, anchor = 'n')

    canva3.create_text(20, 60, text = "Private Room", font = keyfont, anchor = 'nw')
    canva3.create_text(20, 90, text = "Shared Room", font = keyfont, anchor = 'nw')
    canva3.create_text(20, 120, text = "General Ward Bed", font = keyfont, anchor = 'nw')
    canva3.create_text(20, 150, text = "Intensive Care Unit", font = keyfont, anchor = 'nw')

    canva3.create_text(250, 60, text = str(pr), font = valuefont, anchor = 'nw', fill = 'navy')
    canva3.create_text(250, 90, text = str(sr), font = valuefont, anchor = 'nw', fill = 'navy')
    canva3.create_text(250, 120, text = str(gwb), font = valuefont, anchor = 'nw', fill = 'navy')
    canva3.create_text(250, 150, text = str(icu), font = valuefont, anchor = 'nw', fill = 'navy')

    button = Button(dprd, text = 'OK', font = buttonfont, command = dprd.destroy, fg = 'white', bg = 'navy')
    canva3.create_window(175, 200, window = button, anchor = 'n')

    dprd.mainloop()