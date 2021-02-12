from tkinter import *
from tkinter.ttk import *

import csv
import time
import sys
#############################################

counts = 0
count1 = 0


def findnum(IDset):
    x = 0
    i = 0
    t = ''
    global counts,count1

    for n in IDset:

        if(IDbot.get() == str(IDset[x])):
            counts += 1
            Data = [[counts, time.strftime(
                "%D " + "%H"+":"+"%M"+":"+"%S"), IDbot.get(), 1]]
            #print('is Engineering')
            print("No."+str(counts),end=" ")
            print(IDbot.get(),end=" ")
            print(time.strftime("%H"+":"+"%M"+":"+"%S"))
            print("Yes")
            with open('Data1', 'a') as csv_file:
                mydata = csv.writer(csv_file)
                mydata.writerow(Data)
            lable2.config(text='มีสิทธิ์รับเกียร์')
            clearBox()
            i = 1
        x = x + 1
    if(i != 1):
        count1 += 1
        Data = [[count1, time.strftime(
                "%D " + "%H"+":"+"%M"+":"+"%S"), IDbot.get(), 1]]
          #print('is Engineering')
        print("No."+str(count1),end=" ")
        print(IDbot.get(),end=" ")
        print(time.strftime("%H"+":"+"%M"+":"+"%S"))
        print("No!!")
        with open('Data2', 'a') as csv_file:
             mydata = csv.writer(csv_file)
             mydata.writerow(Data)
        lable2.config(text='ไม่มีสิทธิ์')
        clearBox()

def test1(event):
    global IDset
    findnum(IDset)
    clearBox()


def clearBox():
    IDtext.delete(0, END)


#############################################
Screen = Tk()

IDset = []
IDName =[]
CountStudent = 0
Scanner = 0
with open('Database.csv', newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        IDset.append(row['ID'])
        IDName.append(row)
        CountStudent = CountStudent + 1
print(CountStudent)


############################################
IDbot = StringVar()
LBtext = StringVar()
Screen.geometry("500x200")
Screen.title("ระบบเช็คสิทธิ์ งานสร้อยน้องคล้องเกียร์พี่ครั้งที่ 6")
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
