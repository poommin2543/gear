from tkinter import *
from tkinter.ttk import *

import csv
import time
import sys
#############################################

counts = 0


def findnum3(IDset):
    CountStudent = 0
    Scanner = 0
    with open('Data4.csv', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            IDset.append(row['ID'])
            CountStudent = CountStudent + 1
    x = 0
    i = 0
    t = ''
    global counts

    for n in IDset:

        if(IDbot.get() == str(IDset[x])):
            counts += 1
            Data = [[counts, time.strftime(
                "%D " + "%H"+":"+"%M"+":"+"%S"), IDbot.get(),4]]
            print('is Engineering')
            print(time.strftime("%H"+":"+"%M"+":"+"%S"))
            with open('Data', 'a') as csv_file:
                mydata = csv.writer(csv_file)
                mydata.writerow(Data)
            lable2.config(text='กลุ่ม D')
            clearBox()
            i = 1
        x = x + 1
    if(i != 1):
        print('is not Engineering')
        lable2.config(text='ไม่มีสิทธิรับเกียร์')
        clearBox()


def findnum2(IDset):
    CountStudent = 0
    Scanner = 0
    with open('Data3.csv', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            IDset.append(row['ID'])
            CountStudent = CountStudent + 1
    x = 0
    i = 0
    t = ''
    global counts

    for n in IDset:

        if(IDbot.get() == str(IDset[x])):
            counts += 1
            Data = [[counts, time.strftime(
                "%D " + "%H"+":"+"%M"+":"+"%S"), IDbot.get(),3]]
            print('is Engineering')
            print(time.strftime("%H"+":"+"%M"+":"+"%S"))
            with open('Data', 'a') as csv_file:
                mydata = csv.writer(csv_file)
                mydata.writerow(Data)
            lable2.config(text='กลุ่ม C')
            clearBox()
            i = 1
        x = x + 1
    if(i != 1):
       findnum3(IDset)


def findnum1(IDset):
    CountStudent = 0
    Scanner = 0
    with open('Data2.csv', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            IDset.append(row['ID'])
            CountStudent = CountStudent + 1
    x = 0
    i = 0
    t = ''
    global counts

    for n in IDset:

        if(IDbot.get() == str(IDset[x])):
            counts += 1
            Data = [[counts, time.strftime(
                "%D " + "%H"+":"+"%M"+":"+"%S"), IDbot.get(),2]]
            print('is Engineering')
            print(time.strftime("%H"+":"+"%M"+":"+"%S"))
            with open('Data', 'a') as csv_file:
                mydata = csv.writer(csv_file)
                mydata.writerow(Data)
            lable2.config(text='กลุ่ม B')
            clearBox()
            i = 1
        x = x + 1
    if(i != 1):
        findnum2(IDset)


def findnum(IDset):
    CountStudent = 0
    Scanner = 0
    with open('Data1.csv', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            IDset.append(row['ID'])
            CountStudent = CountStudent + 1
    x = 0
    i = 0
    t = ''
    global counts

    for n in IDset:

        if(IDbot.get() == str(IDset[x])):
            counts += 1
            Data = [[counts, time.strftime(
                "%D " + "%H"+":"+"%M"+":"+"%S"), IDbot.get(),1]]
            print('is Engineering')
            print(time.strftime("%H"+":"+"%M"+":"+"%S"))
            with open('Data', 'a') as csv_file:
                mydata = csv.writer(csv_file)
                mydata.writerow(Data)
            lable2.config(text='กลุ่ม A')
            clearBox()
            i = 1
        x = x + 1
    if(i != 1):
        findnum1(IDset)


def test1(event):
    global IDset
    findnum(IDset)
    clearBox()


def clearBox():
    IDtext.delete(0, END)


#############################################
Screen = Tk()

IDset = ['']
'''CountStudent = 0
Scanner = 0
with open('Data1.csv',newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        IDset.append(row['ID'])
        CountStudent = CountStudent + 1
print(CountStudent)'''


############################################
IDbot = StringVar()
LBtext = StringVar()
Screen.geometry("500x200")
Screen.title("ระบบจำแนกกลุ่ม งานสร้อยน้องคล้องเกียร์พี่ครั้งที่ 6")
IDlable = Label(Screen, text="ใส่รหัสนักศึกษา", font=("THsarabunPSK", 20))
IDlable.pack()
lable2 = Label(Screen, text='', font=("THsarabunPSK", 40), anchor='s')

IDtext = Entry(Screen, textvariable=IDbot)
IDtext.pack()

B1 = Button(Screen, text="ตรวจสอบ", command=lambda: findnum(IDset))
print(IDset)
B1.pack()

Screen.bind('<Down>', test1)


lable2.pack()
Screen.mainloop()
