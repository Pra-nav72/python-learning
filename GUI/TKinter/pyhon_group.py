from tkinter import *

win = Tk()

cnv = Canvas(win, width=600, height=3000, bg='white')
cnv.pack(padx=20, pady=20)
px = 0
py = 0


def mouse_down(evt):
    global px, py
    px, py = evt.x, evt.y


def mouse_move(evt):
    global px, py
    cnv.create_line(px, py, evt.x, evt.y, width=2)
    px, py = evt.x, evt.y


cnv.bind('<Button-1>', mouse_down)
cnv.bind('<B1-Motion>', mouse_move)

mainloop()
