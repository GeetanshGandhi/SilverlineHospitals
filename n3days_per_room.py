import mysql.connector as m
from datetime import date
from id_validations import pid_valid
from tk3_daysperroom import *

def days_per_room(discharge, p_id_in=None):
    con = m.connect(host='localhost', user='root', password='mysql', database='silverline_hospital')
    line = con.cursor(buffered=True)
    days_in_pr = 0
    days_in_sr = 0
    days_in_icu = 0
    days_in_gwb = 0
    if p_id_in is None:
        p_id_in = input('Enter Patient ID\n')
        p_id = pid_valid(p_id_in)
    else:
        p_id = p_id_in
    query1 = "select Room_Number from change_transaction where Patient_Id='{}'".format(p_id)
    line.execute(query1)
    res1 = line.fetchall()

    for i in res1:
        query2 = "select Room_Type from room_details where Room_Number='{}'".format(i[0])
        line.execute(query2)
        res2 = line.fetchone()
        room_type = str(res2[0])

        if room_type == 'Private Room':
            query3 = "select Number_of_Days from change_transaction where Room_Number='{}' and Patient_Id='{}' ".format(
                i[0], p_id)
            line.execute(query3)
            res3 = line.fetchall()
            for i in res3:
                for j in i:
                    days_in_pr += j

        elif room_type == 'Shared Room':
            query3 = "select Number_of_Days from change_transaction where Room_Number='{}'and Patient_Id='{}' ".format(
                i[0], p_id)
            line.execute(query3)
            res3 = line.fetchall()
            for i in res3:
                for j in i:
                    days_in_sr += j

        elif room_type == 'General Ward Bed':
            query3 = "select Number_of_Days from change_transaction where Room_Number='{}'and Patient_Id='{}'".format(
                i[0], p_id)
            line.execute(query3)
            res3 = line.fetchall()
            for i in res3:
                for j in i:
                    days_in_gwb += j

        elif room_type == 'Intensive Care Unit':
            query3 = "select Number_of_Days from change_transaction where Room_Number='{}'and Patient_Id='{}'".format(
                i[0], p_id)
            line.execute(query3)
            res3 = line.fetchall()
            for i in res3:
                for j in i:
                    days_in_icu += j

    if discharge == 1:
        query1 = "select MAX(Date_of_Change) from change_transaction where Patient_Id='{}'".format(p_id)
        line.execute(query1)
        res1 = line.fetchone()

        query2 = "select Room_Number from change_transaction where Number_of_Days=1 and Patient_Id = '{}'".format(p_id)
        line.execute(query2)
        res2 = line.fetchone()

        query3 = "select Room_Type from room_details where Room_Number='{}'".format(res2[0])
        line.execute(query3)
        res3 = line.fetchone()

        difference = str(date.today() - res1[0])

        if difference == '0:00:00':
            days_in_latest_room = 1

        elif difference == '1 day, 0:00:00':
            days_in_latest_room = 1

        else:
            prev_days_r = difference[-15::-1]
            prev_days_sl = prev_days_r[::-1]
            days_in_latest_room = int(prev_days_sl)

        if res3[0] == 'Private Room':
            days_in_pr += days_in_latest_room

        elif res3[0] == 'Shared Room':
            days_in_sr += days_in_latest_room

        elif res3[0] == 'General Ward Bed':
            days_in_gwb += days_in_latest_room

        elif res3[0] == 'Intensive Care Unit':
            days_in_icu += days_in_latest_room

    dpr_dict = {'Private Room': [days_in_pr, 3500, days_in_pr * 3500],
                'Shared Room': [days_in_sr, 2700, days_in_sr * 2700],
                'General Ward Bed': [days_in_gwb, 2500, days_in_gwb * 2500],
                'Intensive Care Unit': [days_in_icu, 6000, days_in_icu * 6000]}
    total_days = days_in_sr + days_in_pr + days_in_icu + days_in_gwb
    line.close()
    con.close()
    print(total_days)
    return p_id, days_in_pr, days_in_sr, days_in_gwb, days_in_icu, total_days, dpr_dict

def display_ndays():
    days = list(days_per_room(0))
    days_per_room_display(days[0], days[1], days[2], days[3], days[4])