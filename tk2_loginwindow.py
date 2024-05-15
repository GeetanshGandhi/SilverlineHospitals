from tkinter import *
from tkinter import font as fs
from PIL import Image,ImageTk
import mysql.connector as m

def loginvalid(error = 0):
    global validate
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

    validate = int()
    def validation(event = None): #event to bind enter key to login button
        global user, pw1, validate
        user = userid.get()
        pw1 = password.get()
        if (user == '') or (pw1 == ''):
            validate = 0
        else:
            con = m.connect(host='localhost', user = 'root', password = 'mysql', database = 'silverline_hospital')
            line = con.cursor()
            q = 'select User_Id, Password, Owner from login'
            line.execute(q)
            res = line.fetchall()
            l_user,l_pw,l_owner = [],[],[]
            for i in range(len(res)):
                l_user.append(res[i][0])
                l_pw.append(res[i][1])
                l_owner.append(res[i][2])
            #condtions to display various cred errors
            if (user not in l_user):
                login.destroy()
                loginvalid(error = 1)
            elif (pw1 not in l_pw):
                login.destroy()
                loginvalid(error = 2)
            elif (l_user.index(user)!=l_pw.index(pw1)):
                login.destroy()
                loginvalid(error = 3)
            else: #when creds are completely valid
                validate = 1
                login.destroy()
                print()
                print('Welcome, ', l_owner[l_user.index(user)])
                print()
            line.close()
            con.close()

    def showhide_password(): #to hide or show password
        if pwinp.cget('show') == '':
            pwinp.config(show='*')
            showhide_button.config(text='Show')
        else:
            pwinp.config(show='')
            showhide_button.config(text='Hide')

    headfont = fs.Font(family = "berlin sans fb", size = 24)
    labelfont = fs.Font(family = "algerian", size = 17)
    entryfont = fs.Font(family = "consolas", size = 20)
    buttonfont = fs.Font(family = "consolas", size = 15, weight = "bold")
    errorfont = fs.Font(family = "consolas", size = 12, weight = 'bold')
    minibuttonfont = fs.Font(family = 'arial', size = 10)
    canva2.create_text(150,7,text = "USER LOGIN", font = headfont, fill = "navy", anchor = "n")

    canva2.create_text(150,60, text = "Enter your USER ID", font = labelfont,anchor = "n")
    userinp = Entry(login, width = 5, textvariable = userid, font = entryfont, bg = "lemon chiffon")
    canva2.create_window(150,90, window = userinp, anchor = "n")

    canva2.create_text(150,150, text = "Password", font = labelfont,anchor = "n")
    pwinp = Entry(login, width = 10, textvariable = password, font = entryfont, bg = "lemon chiffon", show = "*")
    canva2.create_window(150,180, window = pwinp, anchor = "n")

    def insertion_when_restart():
        userinp.insert(0,user)
        pwinp.insert(0, pw1)
    if error == 1: #error to be displayed when window ran for 2nd time or thereafter
        canva2.create_text(150, 225, text='Invalid User ID!', font=errorfont, fill='red')
        insertion_when_restart()
    elif error == 2:
        canva2.create_text(150, 225, text='Invalid Password!', font=errorfont, fill='red')
        insertion_when_restart()
    elif error == 3:
        canva2.create_text(150, 225, text='Unmatched Credentials!', font=errorfont, fill='red')
        insertion_when_restart()

    loginbutton = Button(login, text = "LOGIN", command = lambda:validation(),
                         font = buttonfont,fg = "white", bg = "navy",borderwidth = 5)
    canva2.create_window(150, 240, window = loginbutton, anchor = 'n')
    login.bind('<Return>', validation) #binding enter key to login button
    #button to show/hide password
    showhide_button = Button(login, text = 'Show', command = showhide_password, font = minibuttonfont)
    canva2.create_window(250,200, window = showhide_button)
    login.mainloop()

    return validate