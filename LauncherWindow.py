#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Feb 14, 2019 06:15:25 PM CET  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import LauncherWindow_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    LauncherWindow_support.set_Tk_var()
    top = Toplevel1 (root)
    import Launcher as FFF
    FFF.link_with_gui(root, top)
    LauncherWindow_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    LauncherWindow_support.set_Tk_var()
    top = Toplevel1 (w)
    LauncherWindow_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 

        top.geometry("511x327+1247+587")
        top.title("FlyFF Server Starter")
        top.configure(relief="ridge")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.02, rely=0.061, relheight=0.872
                , relwidth=0.47)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Server''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=251)

        self.ServMsg01 = tk.Message(self.Labelframe1)
        self.ServMsg01.place(relx=0.208, rely=0.07, relheight=0.081, relwidth=0.5
                , bordermode='ignore')
        self.ServMsg01.configure(background="#d9d9d9")
        self.ServMsg01.configure(foreground="#000000")
        self.ServMsg01.configure(highlightbackground="#d9d9d9")
        self.ServMsg01.configure(highlightcolor="black")
        self.ServMsg01.configure(text='''Message''')
        self.ServMsg01.configure(width=120)

        self.ServState01 = tk.Message(self.Labelframe1)
        self.ServState01.place(relx=0.75, rely=0.07, relheight=0.081
                , relwidth=0.208, bordermode='ignore')
        self.ServState01.configure(background="#d9d9d9")
        self.ServState01.configure(foreground="#000000")
        self.ServState01.configure(highlightbackground="#d9d9d9")
        self.ServState01.configure(highlightcolor="black")
        self.ServState01.configure(text='''Message''')
        self.ServState01.configure(width=50)

        self.ServCbx01 = tk.Checkbutton(self.Labelframe1)
        self.ServCbx01.place(relx=0.042, rely=0.07, relheight=0.088
                , relwidth=0.088, bordermode='ignore')
        self.ServCbx01.configure(activebackground="#d9d9d9")
        self.ServCbx01.configure(activeforeground="#000000")
        self.ServCbx01.configure(background="#d9d9d9")
        self.ServCbx01.configure(disabledforeground="#a3a3a3")
        self.ServCbx01.configure(foreground="#000000")
        self.ServCbx01.configure(highlightbackground="#d9d9d9")
        self.ServCbx01.configure(highlightcolor="black")
        self.ServCbx01.configure(justify='left')
        self.ServCbx01.configure(variable=LauncherWindow_support.ServC1)

        self.ServCbx02 = tk.Checkbutton(self.Labelframe1)
        self.ServCbx02.place(relx=0.042, rely=0.175, relheight=0.088
                , relwidth=0.088, bordermode='ignore')
        self.ServCbx02.configure(activebackground="#d9d9d9")
        self.ServCbx02.configure(activeforeground="#000000")
        self.ServCbx02.configure(background="#d9d9d9")
        self.ServCbx02.configure(disabledforeground="#a3a3a3")
        self.ServCbx02.configure(foreground="#000000")
        self.ServCbx02.configure(highlightbackground="#d9d9d9")
        self.ServCbx02.configure(highlightcolor="black")
        self.ServCbx02.configure(justify='left')
        self.ServCbx02.configure(variable=LauncherWindow_support.ServC2)

        self.ServCbx03 = tk.Checkbutton(self.Labelframe1)
        self.ServCbx03.place(relx=0.042, rely=0.281, relheight=0.088
                , relwidth=0.088, bordermode='ignore')
        self.ServCbx03.configure(activebackground="#d9d9d9")
        self.ServCbx03.configure(activeforeground="#000000")
        self.ServCbx03.configure(background="#d9d9d9")
        self.ServCbx03.configure(disabledforeground="#a3a3a3")
        self.ServCbx03.configure(foreground="#000000")
        self.ServCbx03.configure(highlightbackground="#d9d9d9")
        self.ServCbx03.configure(highlightcolor="black")
        self.ServCbx03.configure(justify='left')
        self.ServCbx03.configure(variable=LauncherWindow_support.ServC3)

        self.ServCbx04 = tk.Checkbutton(self.Labelframe1)
        self.ServCbx04.place(relx=0.042, rely=0.386, relheight=0.088
                , relwidth=0.088, bordermode='ignore')
        self.ServCbx04.configure(activebackground="#d9d9d9")
        self.ServCbx04.configure(activeforeground="#000000")
        self.ServCbx04.configure(background="#d9d9d9")
        self.ServCbx04.configure(disabledforeground="#a3a3a3")
        self.ServCbx04.configure(foreground="#000000")
        self.ServCbx04.configure(highlightbackground="#d9d9d9")
        self.ServCbx04.configure(highlightcolor="black")
        self.ServCbx04.configure(justify='left')
        self.ServCbx04.configure(variable=LauncherWindow_support.ServC4)

        self.ServCbx05 = tk.Checkbutton(self.Labelframe1)
        self.ServCbx05.place(relx=0.042, rely=0.491, relheight=0.088
                , relwidth=0.088, bordermode='ignore')
        self.ServCbx05.configure(activebackground="#d9d9d9")
        self.ServCbx05.configure(activeforeground="#000000")
        self.ServCbx05.configure(background="#d9d9d9")
        self.ServCbx05.configure(disabledforeground="#a3a3a3")
        self.ServCbx05.configure(foreground="#000000")
        self.ServCbx05.configure(highlightbackground="#d9d9d9")
        self.ServCbx05.configure(highlightcolor="black")
        self.ServCbx05.configure(justify='left')
        self.ServCbx05.configure(variable=LauncherWindow_support.ServC5)

        self.ServCbx06 = tk.Checkbutton(self.Labelframe1)
        self.ServCbx06.place(relx=0.042, rely=0.596, relheight=0.088
                , relwidth=0.088, bordermode='ignore')
        self.ServCbx06.configure(activebackground="#d9d9d9")
        self.ServCbx06.configure(activeforeground="#000000")
        self.ServCbx06.configure(background="#d9d9d9")
        self.ServCbx06.configure(disabledforeground="#a3a3a3")
        self.ServCbx06.configure(foreground="#000000")
        self.ServCbx06.configure(highlightbackground="#d9d9d9")
        self.ServCbx06.configure(highlightcolor="black")
        self.ServCbx06.configure(justify='left')
        self.ServCbx06.configure(variable=LauncherWindow_support.ServC6)

        self.ServCbx07 = tk.Checkbutton(self.Labelframe1)
        self.ServCbx07.place(relx=0.042, rely=0.702, relheight=0.088
                , relwidth=0.088, bordermode='ignore')
        self.ServCbx07.configure(activebackground="#d9d9d9")
        self.ServCbx07.configure(activeforeground="#000000")
        self.ServCbx07.configure(background="#d9d9d9")
        self.ServCbx07.configure(disabledforeground="#a3a3a3")
        self.ServCbx07.configure(foreground="#000000")
        self.ServCbx07.configure(highlightbackground="#d9d9d9")
        self.ServCbx07.configure(highlightcolor="black")
        self.ServCbx07.configure(justify='left')
        self.ServCbx07.configure(variable=LauncherWindow_support.ServC7)

        self.ServMsg02 = tk.Message(self.Labelframe1)
        self.ServMsg02.place(relx=0.208, rely=0.175, relheight=0.081
                , relwidth=0.5, bordermode='ignore')
        self.ServMsg02.configure(background="#d9d9d9")
        self.ServMsg02.configure(foreground="#000000")
        self.ServMsg02.configure(highlightbackground="#d9d9d9")
        self.ServMsg02.configure(highlightcolor="black")
        self.ServMsg02.configure(text='''Message''')
        self.ServMsg02.configure(width=120)

        self.ServMsg03 = tk.Message(self.Labelframe1)
        self.ServMsg03.place(relx=0.208, rely=0.281, relheight=0.081
                , relwidth=0.5, bordermode='ignore')
        self.ServMsg03.configure(background="#d9d9d9")
        self.ServMsg03.configure(foreground="#000000")
        self.ServMsg03.configure(highlightbackground="#d9d9d9")
        self.ServMsg03.configure(highlightcolor="black")
        self.ServMsg03.configure(text='''Message''')
        self.ServMsg03.configure(width=120)

        self.ServMsg04 = tk.Message(self.Labelframe1)
        self.ServMsg04.place(relx=0.208, rely=0.386, relheight=0.081
                , relwidth=0.5, bordermode='ignore')
        self.ServMsg04.configure(background="#d9d9d9")
        self.ServMsg04.configure(foreground="#000000")
        self.ServMsg04.configure(highlightbackground="#d9d9d9")
        self.ServMsg04.configure(highlightcolor="black")
        self.ServMsg04.configure(text='''Message''')
        self.ServMsg04.configure(width=120)

        self.ServMsg05 = tk.Message(self.Labelframe1)
        self.ServMsg05.place(relx=0.208, rely=0.491, relheight=0.081
                , relwidth=0.5, bordermode='ignore')
        self.ServMsg05.configure(background="#d9d9d9")
        self.ServMsg05.configure(foreground="#000000")
        self.ServMsg05.configure(highlightbackground="#d9d9d9")
        self.ServMsg05.configure(highlightcolor="black")
        self.ServMsg05.configure(text='''Message''')
        self.ServMsg05.configure(width=120)

        self.ServMsg06 = tk.Message(self.Labelframe1)
        self.ServMsg06.place(relx=0.208, rely=0.596, relheight=0.081
                , relwidth=0.5, bordermode='ignore')
        self.ServMsg06.configure(background="#d9d9d9")
        self.ServMsg06.configure(foreground="#000000")
        self.ServMsg06.configure(highlightbackground="#d9d9d9")
        self.ServMsg06.configure(highlightcolor="black")
        self.ServMsg06.configure(text='''Message''')
        self.ServMsg06.configure(width=120)

        self.ServMsg07 = tk.Message(self.Labelframe1)
        self.ServMsg07.place(relx=0.208, rely=0.702, relheight=0.081
                , relwidth=0.5, bordermode='ignore')
        self.ServMsg07.configure(background="#d9d9d9")
        self.ServMsg07.configure(foreground="#000000")
        self.ServMsg07.configure(highlightbackground="#d9d9d9")
        self.ServMsg07.configure(highlightcolor="black")
        self.ServMsg07.configure(text='''Message''')
        self.ServMsg07.configure(width=120)

        self.ServState02 = tk.Message(self.Labelframe1)
        self.ServState02.place(relx=0.75, rely=0.175, relheight=0.081
                , relwidth=0.208, bordermode='ignore')
        self.ServState02.configure(background="#d9d9d9")
        self.ServState02.configure(foreground="#000000")
        self.ServState02.configure(highlightbackground="#d9d9d9")
        self.ServState02.configure(highlightcolor="black")
        self.ServState02.configure(text='''Message''')
        self.ServState02.configure(width=50)

        self.ServState03 = tk.Message(self.Labelframe1)
        self.ServState03.place(relx=0.75, rely=0.281, relheight=0.081
                , relwidth=0.208, bordermode='ignore')
        self.ServState03.configure(background="#d9d9d9")
        self.ServState03.configure(foreground="#000000")
        self.ServState03.configure(highlightbackground="#d9d9d9")
        self.ServState03.configure(highlightcolor="black")
        self.ServState03.configure(text='''Message''')
        self.ServState03.configure(width=50)

        self.ServState04 = tk.Message(self.Labelframe1)
        self.ServState04.place(relx=0.75, rely=0.386, relheight=0.081
                , relwidth=0.208, bordermode='ignore')
        self.ServState04.configure(background="#d9d9d9")
        self.ServState04.configure(foreground="#000000")
        self.ServState04.configure(highlightbackground="#d9d9d9")
        self.ServState04.configure(highlightcolor="black")
        self.ServState04.configure(text='''Message''')
        self.ServState04.configure(width=50)

        self.ServState05 = tk.Message(self.Labelframe1)
        self.ServState05.place(relx=0.75, rely=0.491, relheight=0.081
                , relwidth=0.208, bordermode='ignore')
        self.ServState05.configure(background="#d9d9d9")
        self.ServState05.configure(foreground="#000000")
        self.ServState05.configure(highlightbackground="#d9d9d9")
        self.ServState05.configure(highlightcolor="black")
        self.ServState05.configure(text='''Message''')
        self.ServState05.configure(width=50)

        self.ServState06 = tk.Message(self.Labelframe1)
        self.ServState06.place(relx=0.75, rely=0.596, relheight=0.081
                , relwidth=0.208, bordermode='ignore')
        self.ServState06.configure(background="#d9d9d9")
        self.ServState06.configure(foreground="#000000")
        self.ServState06.configure(highlightbackground="#d9d9d9")
        self.ServState06.configure(highlightcolor="black")
        self.ServState06.configure(text='''Message''')
        self.ServState06.configure(width=50)

        self.ServState07 = tk.Message(self.Labelframe1)
        self.ServState07.place(relx=0.75, rely=0.702, relheight=0.081
                , relwidth=0.208, bordermode='ignore')
        self.ServState07.configure(background="#d9d9d9")
        self.ServState07.configure(foreground="#000000")
        self.ServState07.configure(highlightbackground="#d9d9d9")
        self.ServState07.configure(highlightcolor="black")
        self.ServState07.configure(text='''Message''')
        self.ServState07.configure(width=50)

        self.ServStart = tk.Button(self.Labelframe1)
        self.ServStart.place(relx=0.042, rely=0.807, height=44, width=97
                , bordermode='ignore')
        self.ServStart.configure(activebackground="#ececec")
        self.ServStart.configure(activeforeground="#000000")
        self.ServStart.configure(background="#d9d9d9")
        self.ServStart.configure(disabledforeground="#a3a3a3")
        self.ServStart.configure(foreground="#000000")
        self.ServStart.configure(highlightbackground="#d9d9d9")
        self.ServStart.configure(highlightcolor="black")
        self.ServStart.configure(pady="0")
        self.ServStart.configure(text='''Start''')

        self.ServStop = tk.Button(self.Labelframe1)
        self.ServStop.place(relx=0.542, rely=0.807, height=44, width=97
                , bordermode='ignore')
        self.ServStop.configure(activebackground="#ececec")
        self.ServStop.configure(activeforeground="#000000")
        self.ServStop.configure(background="#d9d9d9")
        self.ServStop.configure(disabledforeground="#a3a3a3")
        self.ServStop.configure(foreground="#000000")
        self.ServStop.configure(highlightbackground="#d9d9d9")
        self.ServStop.configure(highlightcolor="black")
        self.ServStop.configure(pady="0")
        self.ServStop.configure(text='''Stop''')

        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.509, rely=0.061, relheight=0.749
                , relwidth=0.47)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Client''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")
        self.Labelframe2.configure(width=240)

        self.ClientState2 = tk.Message(self.Labelframe2)
        self.ClientState2.place(relx=0.042, rely=0.204, relheight=0.094
                , relwidth=0.917, bordermode='ignore')
        self.ClientState2.configure(background="#d9d9d9")
        self.ClientState2.configure(foreground="#000000")
        self.ClientState2.configure(highlightbackground="#d9d9d9")
        self.ClientState2.configure(highlightcolor="black")
        self.ClientState2.configure(text='''Message''')
        self.ClientState2.configure(width=220)

        self.ClientStartBig = tk.Button(self.Labelframe2)
        self.ClientStartBig.place(relx=0.042, rely=0.49, height=34, width=217
                , bordermode='ignore')
        self.ClientStartBig.configure(activebackground="#ececec")
        self.ClientStartBig.configure(activeforeground="#000000")
        self.ClientStartBig.configure(background="#d9d9d9")
        self.ClientStartBig.configure(disabledforeground="#a3a3a3")
        self.ClientStartBig.configure(foreground="#000000")
        self.ClientStartBig.configure(highlightbackground="#d9d9d9")
        self.ClientStartBig.configure(highlightcolor="black")
        self.ClientStartBig.configure(pady="0")
        self.ClientStartBig.configure(text='''Start''')

        self.ClientKill = tk.Button(self.Labelframe2)
        self.ClientKill.place(relx=0.042, rely=0.816, height=34, width=217
                , bordermode='ignore')
        self.ClientKill.configure(activebackground="#ececec")
        self.ClientKill.configure(activeforeground="#000000")
        self.ClientKill.configure(background="#d9d9d9")
        self.ClientKill.configure(disabledforeground="#a3a3a3")
        self.ClientKill.configure(foreground="#000000")
        self.ClientKill.configure(highlightbackground="#d9d9d9")
        self.ClientKill.configure(highlightcolor="black")
        self.ClientKill.configure(pady="0")
        self.ClientKill.configure(text='''Kill all''')

        self.ClientUpdate = tk.Button(self.Labelframe2)
        self.ClientUpdate.place(relx=0.042, rely=0.653, height=34, width=217
                , bordermode='ignore')
        self.ClientUpdate.configure(activebackground="#ececec")
        self.ClientUpdate.configure(activeforeground="#000000")
        self.ClientUpdate.configure(background="#d9d9d9")
        self.ClientUpdate.configure(disabledforeground="#a3a3a3")
        self.ClientUpdate.configure(foreground="#000000")
        self.ClientUpdate.configure(highlightbackground="#d9d9d9")
        self.ClientUpdate.configure(highlightcolor="black")
        self.ClientUpdate.configure(pady="0")
        self.ClientUpdate.configure(text='''Kill and Update''')

        self.ClientState = tk.Message(self.Labelframe2)
        self.ClientState.place(relx=0.042, rely=0.082, relheight=0.094
                , relwidth=0.917, bordermode='ignore')
        self.ClientState.configure(background="#d9d9d9")
        self.ClientState.configure(foreground="#000000")
        self.ClientState.configure(highlightbackground="#d9d9d9")
        self.ClientState.configure(highlightcolor="black")
        self.ClientState.configure(text='''Message''')
        self.ClientState.configure(width=220)

        self.ClientIni = tk.Button(self.Labelframe2)
        self.ClientIni.place(relx=0.042, rely=0.327, height=34, width=217
                , bordermode='ignore')
        self.ClientIni.configure(activebackground="#ececec")
        self.ClientIni.configure(activeforeground="#000000")
        self.ClientIni.configure(background="#d9d9d9")
        self.ClientIni.configure(disabledforeground="#a3a3a3")
        self.ClientIni.configure(foreground="#000000")
        self.ClientIni.configure(highlightbackground="#d9d9d9")
        self.ClientIni.configure(highlightcolor="black")
        self.ClientIni.configure(pady="0")
        self.ClientIni.configure(text='''Open Ini File''')

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.509, rely=0.856, relheight=0.07
                , relwidth=0.47)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''FlyFF Server Launcher by SquonK, 2019''')
        self.Message1.configure(width=240)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="{Segoe UI} 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





