#menu driven main programme
print('''MENU
1.) Press 1 for Admission Form
2.) Press 2 for Patient Details
3.) Press 3 for Bill Details
4.) Press 4 to View Bank Details
5.) Press 5 to Know About Available Rooms
6.) Press 6 to Know View Available Treatments
7.) Press 7 to Login as Administrator''')

choice_inp = input('Enter your choice\n')
while choice_inp.isdigit()==False or choice_inp not in ["1", "2", "3", "4", "5", "6","7"]:
    choice_inp = input("Invalid choice! Kindly Re-Enter:\n ")
else:
    choice = int(choice_inp)
if choice == 1:
    from n1registeration import *
    registeration()

elif choice == 2:
    from n2patient_details import *
    p_details()
elif choice == 3:
    from tk4_bill_display import billdisplay
    billdisplay(b_id_input=None)
elif choice == 4:
    from tk5_bank_details import bank_details
    bank_details(0)
elif choice == 5:
    from tk7_room_details import *
    room_details(dependency=0)
elif choice == 6:
    from tk8_trt_details import *
    trt_det(dependency=0)
elif choice == 7:
    from tk2_loginwindow import *
    #checking if login was validated
    check = loginvalid()
    loop = 1
    if check == 0:
        print('Please login to continue!')
        loop=0
    while loop == 1:
        print('''MENU
1.)  Press 1 for Admission Form
2.)  Press 2 for Patient Details
3.)  Press 3 for Bill Details
4.)  Press 4 for Bank Details
5.)  Press 5 for Discharge Form
6.)  Press 6 to Add a Doctor
7.)  Press 7 to Add an Administrator
8.)  Press 8 to Add a New Treatment
9.)  Press 9 to Check Days per Room for a Patient
10.) Press 10 to Change the Room for a Patient
11.) Press 11 to View Available Rooms
12.) Press 12 to View Available Treatments
13.) Press 13 to Update Payment Status for a Bill
        ''')
        choice_inp = input('Enter your choice\n')
        while choice_inp.isdigit()==False or choice_inp not in ['1','2','3','4','5','6','7','8','9','10','11','12','13']:
            choice_inp = input('Invalid Choice! Kindly Re-Enter:\n')
        else:
            choice = int(choice_inp)
        if choice == 1:
            from n1registeration import *
            registeration()
        elif choice == 2:
            from n2patient_details import *
            p_details()
        elif choice==3:
            from tk4_bill_display import billdisplay
            billdisplay(b_id_input=None)
        elif choice == 4:
            from tk5_bank_details import *
            bank_details(dependency=0)
        elif choice == 5:
            from n5discharge_form import *
            discharge()
        elif choice == 6:
            from n10add_doctors import *
            add_doc()
        elif choice == 7:
            from n11add_adm import *
            add_adm()
        elif choice == 8:
            from n12add_trtmnt import *
            add_trt()
        elif choice == 9:
            from n3days_per_room import display_ndays
            display_ndays()
        elif choice == 10:
            from n4up_room import *
            up_roomno()
        elif choice == 11:
            from tk7_room_details import *
            room_details(dependency=0)
        elif choice == 12:
            from tk8_trt_details import *
            trt_det(dependency=0)
        elif choice == 13:
            from n9bill_status_change import billstatus
            billstatus()

        cont = input("You want to continue?(y/n)")
        while cont != "y" and cont != "Y" and cont != "N" and cont != "n":
            cont = input("Invalid choice, enter again!(y/n)")
        else:
            if cont == "y" or cont == "Y":
                continue
            elif cont == "n" or cont == "N":
                loop = 0
else:
    print('Invalid choice. The menu now terminates')