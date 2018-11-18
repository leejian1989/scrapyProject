#!/usr/bin/python
#-*- coding: UTF-8 -*-

from Tkinter import *

def cb(event):
    print "vaiable is ",



root =Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
li=[]

file=open('daily.log')
for line in file.xreadlines():
    li.append(line)

movie=['css','jquery','bootsrap']

listb=Listbox(root)
listb2=Listbox(root)
c=[]
v=[]

def check_box(event=None):
    print 'check_box'
    for i in xrange(len(li)):
        #print v[i].get()
        if v[i].get() ==1:
            print li[i]

for i in xrange(len(li)):
    print i
    var=IntVar()
    ci=Checkbutton(root,text=li[i],variable=var)
    v.append(var)
    c.append(ci)
    ci.pack()




'''for item in li:

    listb.insert(0,item)


for item in movie:
    listb2.insert(0,item)
'''
button=Button(root,text='OK',command=check_box)

#listb.pack()
#listb2.pack()
button.pack()
#root.grid()
root.mainloop()