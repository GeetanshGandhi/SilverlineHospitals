from tkinter import *
from tkinter import messagebox
from tkinter import font as fs
from PIL import Image,ImageTk
import mysql.connector as m

def loginvalid(error = 0):
    login = Tk()
    login.geometry("300x300")
    login.configure(bg = "navy")
    login.title("Admin\'s Login")
    login.resizable(False, False)

    img_open = Image.open("Slide1.jpg")
    resize = img_open.resize((300,300), Image.ANTIALIAS)
    img_openre = ImageTk.PhotoImage(resize)

    canva2 = Canvas(login, width = 300, height = 300, highlightthickness = 0)
    canva2.pack(fill = "both", expand = True)
    canva2.configure(bg = "navy")
    canva2.create_image(0,0, image = img_openre, anchor = "nw")
    userid = StringVar()
    password = StringVar()

    def validation(event = None): #event to bind enter key to login button
        global user, pw1
        user = userid.get()
        pw1 = password.get()
        con = m.connect(host='localhost', user = 'root', password = 'mysql', database = 'silverline_hospital')
        line = con.cursor()
        q = 'select User_Id, Password, Owner from login'
        line.execute(q)
        res = line.fetchall()
        l_user = []
        l_pw =[]
        l_owner = []
        for i in range(len(res)):
            l_user.append(res[i][0])
            l_pw.append(res[i][1])
            l_owner.append(res[i])
        if (user not in l_user) or (pw1 not in l_pw) or (l_user.index(user)!=l_pw.index(pw1)):
            login.destroy()
            loginvalid(error = 1)
        else:
            print()
            print('Welcome, ', l_owner[l_user.index(user)][2])
            print()
            login.destroy()
        line.close()
        con.close()

    headfont = fs.Font(family = "berlin sans fb", size = 24)
    labelfont = fs.Font(family = "algerian", size = 17)
    entryfont = fs.Font(family = "consolas", size = 20)
    buttonfont = fs.Font(family = "consolas", size = 15, weight = "bold")
    errorfont = fs.Font(family = "consolas", size = 12, weight = 'bold')
    canva2.create_text(150,7,text = "USER LOGIN", font = headfont, fill = "navy", anchor = "n")

    canva2.create_text(150,60, text = "Enter your USER ID", font = labelfont,anchor = "n")
    userinp = Entry(login, width = 5, textvariable = userid, font = entryfont, bg = "lemon chiffon")
    canva2.create_window(150,90, window = userinp, anchor = "n")

    canva2.create_text(150,150, text = "Password", font = labelfont,anchor = "n")
    pwinp = Entry(login, width = 10, textvariable = password, font = entryfont, bg = "lemon chiffon", show = "*")
    canva2.create_window(150,180, window = pwinp, anchor = "n")

    if error == 1:
        canva2.create_text(150, 225, text='Invalid User ID or Password', font=errorfont, fill='red')
        userinp.insert(0, user)
        pwinp.insert(0, pw1)
    loginbutton = Button(login, text = "LOGIN", command = lambda:[validation()],
                         font = buttonfont,fg = "white", bg = "navy",borderwidth = 5)
    canva2.create_window(150, 240, window = loginbutton, anchor = 'n')
    login.bind('<Return>', validation) #binding enter key to login button
    login.mainloop()