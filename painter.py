from tkinter import *

root = Tk()
root.title("Painter")
root.geometry("800x600")
w=600
h=400
canvas = Canvas(root,width=w,height=h,bg="white")
canvas.pack(pady=20)



root.mainloop()