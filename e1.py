
from Tkinter import *
import os
import requests
import time
import Tkinter as tk
import serial
import threading
from threading import Thread


dweetIO="https://dweet.io/dweet/for/"
ph2="ph"
do2="do"
con2="con"
orp2="orp"
temp2="temp"
myName="watersensor"
ser1 = serial.Serial('/dev/ttyUSB0', 9600)
#ser2 = serial.Serial('/dev/ttyAMA0', 115200)
running = True  # Global flag

def getSensor():
    waktu = time.strftime ("%Y-%m-%d,%H:%M:%S,",time.gmtime())
    respon1 = ser1.readline()
    respon1 = respon1[respon1.find("#")+1:respon1.find("*")]
    #respon2 = ser2.readline()
    listsensor = respon1.split (',')
    global ph,do,con,orp,temp
    ph=listsensor[1]
    do=listsensor[6]
    con=listsensor[2]
    orp=listsensor[0]
    temp=listsensor[7]

    ph1.set(str(ph))
    do1.set(str(do))
    con1.set(str(con))
    orp1.set(str(orp))
    temp1.set(str(temp))
    
    print waktu,respon1
    
    
def kirim():
    try:
        global running
        while running:
            getSensor()
            rqsString = dweetIO+myName+'?'+ph2+'='+str(ph)+'&'+do2+'='+str(do)+'&'+con2+'='+str(con)+'&'+orp2+'='+str(orp)+'&'+temp2+'='+str(temp)
            rqs = requests.get(rqsString)       
            time.sleep(1)
            status.set(str("berhasil"))
            root.update()
    except:
        status.set(str("gagal"))
        
def baca():
    global running
    running = True
    while running:
        Thread(target = getSensor()).start()
        time.sleep(1)
        root.update()

def kirim2():
    global running
    running = True
    Thread(target = kirim()).start()
    Thread(target = get_sensor()).start()
    
    
def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False

def close_window(): 
    root.destroy()

def hover1(event):
    btn1.configure(bg='red',fg='white')
def hover2(event):
    btn2.configure(bg='red',fg='white')
def hover3(event):
    btn3.configure(bg='red',fg='white')
def hover4(event):
    btn4.configure(bg='red',fg='white')
def hover5(event):
    btn5.configure(bg='red',fg='white')

def hover21(event):
    btn1.configure(bg=defaultbg,fg='black')
def hover22(event):
    btn2.configure(bg=defaultbg,fg='black')
def hover23(event):
    btn3.configure(bg=defaultbg,fg='black')
def hover24(event):
    btn4.configure(bg=defaultbg,fg='black')
def hover25(event):
    btn5.configure(bg=defaultbg,fg='black')


root = tk.Tk()
root.title('Compact Fixed Position Water Monitoring Sensor')
root.attributes('-fullscreen', True)

defaultbg = root.cget('bg')
f2=LabelFrame(root,text='Result')
ph1=StringVar()
do1=StringVar()
con1=StringVar()
orp1=StringVar()
temp1=StringVar()
status=StringVar()

phframe=LabelFrame(f2,text="ph",bg='red',font=("Arial",14))
Label(phframe,bg="white",textvariable=ph1,font=("Arial",16)).pack(fill=BOTH,expand=YES,side=LEFT)
phframe.grid(column=0,row=1,sticky="nsew",padx=4,pady=4)

doframe=LabelFrame(f2,text='do',bg='yellow',font=("Arial",14))
Label(doframe,bg="white",textvariable=do1,font=("Arial",16)).pack(fill=BOTH,expand=YES,side=LEFT)
doframe.grid(column=1,row=1,sticky="nsew",padx=4,pady=4)

orpframe=LabelFrame(f2,text='orp',width=21,bg='cyan',font=("Arial",14))
Label(orpframe,bg="white",textvariable=orp1,font=("Arial",16)).pack(fill=BOTH,expand=YES,side=LEFT)
orpframe.grid(column=0,row=2,sticky="nsew",padx=4,pady=4)

conframe=LabelFrame(f2,text='con',width=21,bg='green',font=("Monospace",14))
Label(conframe,bg="white",textvariable=con1,font=("Arial",16)).pack(fill=BOTH,expand=YES,side=LEFT)
conframe.grid(column=1,row=2,sticky="nsew",padx=4,pady=4)

tempframe=LabelFrame(f2,text='temp',width=21,bg='brown',fg="white",font=("Monospace",14))
Label(tempframe,bg="white",textvariable=temp1,font=("Arial",16)).pack(fill=BOTH,expand=YES,side=LEFT)
tempframe.grid(column=2,row=1,sticky="nsew",padx=4,pady=4)

f2.columnconfigure(0, weight=1)
f2.columnconfigure(1, weight=1)
f2.columnconfigure(2, weight=1)
f2.rowconfigure(0, weight=0) # not needed, this is the default behavior
f2.rowconfigure(1, weight=1)
f2.rowconfigure(2, weight=1)

f2.grid(column=0,row=1,sticky="nsew",padx=4)


f3=LabelFrame(root,text='Status',font=("Arial",16))
Label(f3,bg="white",width=20,textvariable=status,height=3).pack(fill=BOTH,expand=YES,side=LEFT)
f3.grid(column=0,row=2,sticky=EW)


f=Frame(root,width=21)
btn1=Button(f,text='Connect',cursor="hand2",font=("helvetica",30))
btn1.bind('<Enter>',hover1)
btn1.bind('<Leave>',hover21)
btn1.pack(fill=BOTH,expand=YES)

btn2=Button(f,text='Get Sensor',command=baca,cursor="hand2",font=("helvetica",30))
btn2.bind('<Enter>',hover2)
btn2.bind('<Leave>',hover22)
btn2.pack(fill=BOTH,expand=YES)

btn3=Button(f,text='Send',command=kirim2,cursor="hand2",font=("helvetica",30))
btn3.bind('<Enter>',hover3)
btn3.bind('<Leave>',hover23)
btn3.pack(fill=BOTH,expand=YES)

btn4=Button(f,text='Stop',cursor="hand2",command=stop,font=("helvetica",30))
btn4.bind('<Enter>',hover4)
btn4.bind('<Leave>',hover24)
btn4.pack(fill=BOTH,expand=YES)

f.grid(column=1,row=1,columnspan=2,sticky=NSEW)

f4=Frame(root)
btn5=Button(f4,text='Exit',command=close_window,cursor="hand2",font=("helvetica",30))
btn5.bind('<Enter>',hover5)
btn5.bind('<Leave>',hover25)
btn5.pack(fill=BOTH,expand=YES)
f4.grid(column=1,row=2,columnspan=2,sticky=EW)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0) # not needed, this is the default behavior
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

mainloop()
