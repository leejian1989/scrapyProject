import Tkinter as tk
import string
import sys
import MySQLdb
import time
import datetime

class ScrollableFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        # create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(side='right', fill="y",  expand="false")
        self.canvas = tk.Canvas(self,
                                bg='#444444', bd=0,
                                height=550,
                                width=1000,
                                highlightthickness=0,
                                yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side="left", fill="both", expand="true")
        self.vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas, **kwargs)
        self.canvas.create_window(0, 0, window=self.interior, anchor="nw")

        self.bind('<Configure>', self.set_scrollregion)


    def set_scrollregion(self, event=None):
        """ Set the scroll region on the canvas"""
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

def check_box(event=None):
    print 'check_box'
    file1=open('cheat.log','w')
    count=1
    for i in xrange(len(li)):
        #print v[i].get()
        if v[i].get() ==1:
            print li[i]
            file1.write(str(count)+':'+li[i]+'\n')
            count=count+1

            pos = li[i].find('http')
            # print  "pos",pos
            title = li[i][:pos]
            link = li[i][pos:]
            # print 'link',link
            title_hash = hash(title)
            # print datetime.date.today()
            sql = '''insert into  daily_reports(s_date,title,link,title_hash,report_type)values ('%s','%s','%s','%s','%s')
                        ''' % (datetime.date.today(), title, link, title_hash, 'cheat')

            try:
                cursor.execute(sql)
                conn.commit()
            except Exception, e:
                conn.rollback()
                print 'fucking error', e
    # after click the 'ok' button, then quit out !
    root.destroy()

try:
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='dailyreport')
except Exception, e:
    print  'exception:', e

    sys.exit()

cursor = conn.cursor()

def GetDate(delta=0):
    dt=datetime.datetime.now()
    dt=dt+datetime.timedelta(days=-delta)
    return dt.strftime('%Y%m%d')

if __name__ == '__main__':
    root = tk.Tk()
    checkbox_pane = ScrollableFrame(root, bg='#444444')
    checkbox_pane.pack(expand="true", fill="both")

    '''def button_callback():
        for x in range(1,50):
            tk.Checkbutton(checkbox_pane.interior, text="hello world! %s" % x).grid(row=x, column=0)

    btn_checkbox = tk.Button(checkbox_pane.interior, text="Click Me!", command=button_callback)
    btn_checkbox.grid(row=0, column=0)'''
    li=[]
    v=[]
    c=[]

    hash_selected = []

    sql = "select title_hash from daily_reports where s_date>=%s and report_type='cheat' " % (GetDate(7))
    cursor.execute(sql)
    alldata1 = cursor.fetchall()
    if alldata1:
        for rec in alldata1:
            hash_selected.append(rec[0])

    # print  'hash_selected',hash_selected
    # print 'get date',GetDate(0)
    sql = "select title,link,title_hash,source from dailycheat where s_date=%s" % (GetDate(0))
    cursor.execute(sql)
    alldata = cursor.fetchall()
    if alldata:
        for rec in alldata:
            # print 'title_hash',rec[2]
            has_reported = False
            for h in hash_selected:
                if str(h) == str(rec[2]):
                    has_reported = True
                    break
            if has_reported == False:
                li.append( rec[0] + rec[1])

    '''
    file = open('cheat.txt')
    for line in file.xreadlines():
        li.append(line)
    '''
    for i in xrange(len(li)):
        #print i
        var = tk.IntVar()
        ci = tk.Checkbutton(checkbox_pane.interior, text=li[i], variable=var)
        v.append(var)
        c.append(ci)
        ci.pack()

    button = tk.Button(root, text='OK', command=check_box)
    button.pack()

    root.mainloop()