from tkinter import *

root = Tk()
root.title("Painter")
root.geometry("800x600")

def paint(e):
    x1=e.x -1
    y1=e.y -1
    
    x2=e.x +1
    y2 = e.y+1
    
    canvas.create_line(x1,y1,x2,y2,fill="green")

w=600
h=400
canvas = Canvas(root,width=w,height=h,bg="white")
canvas.pack(pady=20)

canvas.bind('<B1-Motion>',paint)

root.mainloop()