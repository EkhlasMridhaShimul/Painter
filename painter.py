from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Painter")
root.geometry("800x800")

def paint(e):
    brushSize= int(myslider.get())
    brushColor="blue"
    #brush types: ROUND, ROUND, PROJECTING
    brushType=brush_type.get()
    
    x1=e.x -1
    y1=e.y -1
    
    x2=e.x +1
    y2 = e.y+1
    
    canvas.create_line(x1,y1,x2,y2,fill=brushColor,width=brushSize,capstyle=brushType,smooth=True)


def change_brush_size(data):
    sliderLabel.config(text=int(myslider.get()))

w=600
h=400
canvas = Canvas(root,width=w,height=h,bg="white")
canvas.pack(pady=20)

canvas.bind('<B1-Motion>',paint)

brushOptionsFrame = Frame(root,bg="green")
brushOptionsFrame.pack(pady=20)

brushSizeFrame= LabelFrame(brushOptionsFrame,text="Brush size")
brushSizeFrame.grid(row=0,column=0,padx=20)

myslider = ttk.Scale(brushSizeFrame,from_=1,to=100,command=change_brush_size,orient=VERTICAL,value=10)
myslider.pack(pady=10,padx=10)

sliderLabel = Label(brushSizeFrame,text=myslider.get())
sliderLabel.pack(pady=5)

brushTypeFrame = LabelFrame(brushOptionsFrame,text="Brush type")
brushTypeFrame.grid(row=0,column=1,padx=20)

brush_type = StringVar()
brush_type.set("round")

brushTypeRound = Radiobutton(brushTypeFrame,text="Round",variable=brush_type,value="round")
brushTypeSlash = Radiobutton(brushTypeFrame,text="Slash",variable=brush_type,value="butt")
brushTypeDiamond = Radiobutton(brushTypeFrame,text="Diamond",variable=brush_type,value="projecting")

brushTypeRound.pack(anchor=W)
brushTypeSlash.pack(anchor=W)
brushTypeDiamond.pack(anchor=W)

root.mainloop()