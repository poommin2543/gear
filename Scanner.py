from tkinter import *
from tkinter.ttk import *

import csv
import time
import sys

##IDset = []
##CountStudent = 0
##Scanner = 0
##with open('Data.csv',newline="") as csvfile:
##    reader = csv.DictReader(csvfile)
##    for row in reader:
##        IDset.append(row['ID'])
##        CountStudent = CountStudent + 1 
        
#print(IDset)
            

counts = 0
#x = number student , ID = ID , IDset = Data 
def findnum(IDset): 
    x = 0
    i = 0
    t= ''
    global counts 
    
    
    for n in IDset:
        if(IDbot.get() == str(IDset[x])):
            counts +=1
            Data =[[counts,time.strftime("%H"+":"+"%M"+":"+"%S"),IDbot.get()]]
            print('is Engineering')
            print(time.strftime("%H"+":"+"%M"+":"+"%S"))
            with open('221','a') as csv_file:
                my221 = csv.writer(csv_file)
                my221.writerow(Data)
            lable2.config(text = 'วิศวกรรมศาสตร์')
            
            
            
            i = 1
        x = x + 1
    if(i != 1):
        print('is not Engineering')
        lable2.config(text = 'ไม่ใช่วิศวกรรมศาสตร์')
    
    
 
def scanner():
    x = ''
    while(x != 'X'):
        ID = input(IDtext,":")
        findnum(CountStudent,ID,IDset)

def test1 (event):
    global IDset
    findnum(IDset)
    clearBox()
    
    
    
def clearBox():
    IDtext.delete(0,END)
    
        

#############################################
Screen = Tk()

IDset = []
CountStudent = 0
Scanner = 0
with open('Data.csv',newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        IDset.append(row['ID'])
        CountStudent = CountStudent + 1
print(CountStudent)

############################################
IDbot = StringVar()
LBtext = StringVar()
Screen.geometry("500x200")
Screen.title("ระบบลงทะเบียน งานสร้อยน้องคล้องเกียร์พี่ครั้งที่ 4")
IDlable = Label(Screen,text = "ใส่รหัสนักศึกษา",font=("THsarabunPSK",20))
IDlable.pack()
lable2 = Label(Screen,text = '',font=("THsarabunPSK",40),anchor = 's')

IDtext=Entry(Screen,textvariable=IDbot)
IDtext.pack()
B1 = Button(Screen,text="ตรวจสอบ",command = lambda:findnum(IDset))
B1.pack()
clearBox()
Screen.bind('<Down>',test1)


lable2.pack()
Screen.mainloop()


        

