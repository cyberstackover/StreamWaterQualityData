
from Tkinter import *
import os
import requests
import time
import Tkinter as tk

dweetIO="https://dweet.io/dweet/for/"
kunci="cpu"
myName="watersensor"


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
        
def baca():
    global a
    a=getCPUtemperature()
    for i in range(50):
        ph.set(str(a))
        print a
        time.sleep(1)
        root.update()
def kirim():
    try:
        for i in range(50):
            rqsString = dweetIO+myName+'?'+kunci+'='+str(a)
            rqs = requests.get(rqsString)
            status.set(str("berhasil"))
    except:
        status.set(str("gagal"))


root = tk.Tk()
root.title('Compact Fixed Position Water Monitoring Sensor')

f2=LabelFrame(root,text='Result')
ph=StringVar()
status=StringVar()

phframe=LabelFrame(f2,text="ph",bg='red',font=("Arial",14))
Label(phframe,bg="white",textvariable=ph,font=("Arial",16)).pack(fill=BOTH,expand=YES,side=LEFT)
phframe.grid(column=0,row=1,sticky="nsew",padx=4,pady=4)

doframe=LabelFrame(f2,text='do',bg='green',font=("Arial",14))
Label(doframe,bg="white",textvariable=ph,font=("Arial",16)).pack(fill=BOTH,expand=YES,side=LEFT)
doframe.grid(column=1,row=1,sticky="nsew",padx=4,pady=4)

orpframe=LabelFrame(f2,text='orp',width=21,bg='cyan',font=("Arial",14))
Label(orpframe,bg="white",textvariable=ph,font=("Arial",16)).pack(fill=BOTH,expand=YES,side=LEFT)
orpframe.grid(column=0,row=2,sticky="nsew",padx=4,pady=4)

conframe=LabelFrame(f2,text='con',width=21,bg='yellow',font=("Monospace",14))
Label(conframe,bg="white",textvariable=ph).pack(fill=BOTH,expand=YES,side=LEFT)
conframe.grid(column=1,row=2,sticky="nsew",padx=4,pady=4)

f2.columnconfigure(0, weight=1)
f2.columnconfigure(1, weight=1)
f2.rowconfigure(0, weight=0) # not needed, this is the default behavior
f2.rowconfigure(1, weight=1)
f2.rowconfigure(2, weight=1)

f2.grid(column=0,row=1,sticky="nsew",padx=4)


f3=LabelFrame(root,text='Status',font=("Arial",14))
Label(f3,bg="white",width=20,textvariable=status).pack(fill=BOTH,expand=YES,side=LEFT)
f3.grid(column=0,row=2,sticky=EW)


f=Frame(root,width=21)
Button(f,text='Connect',width=50).pack(fill=BOTH,expand=YES)
Button(f,text='Get Sensor',width=50,command=baca).pack(fill=BOTH,expand=YES)
Button(f,text='Send',width=50,command=kirim).pack(fill=BOTH,expand=YES)
Button(f,text='Stop',width=50).pack(fill=BOTH,expand=YES)
f.grid(column=1,row=1,columnspan=2,sticky=NSEW)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0) # not needed, this is the default behavior
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

mainloop()
