import tkinter as tk
import csv
from PIL import ImageTk,Image
root = tk.Tk()
f=tk.Frame(root)
f.pack
ima = Image.open("D:\\imdge.png")
im = ImageTk.PhotoImage(ima)
l = tk.Label(root,image=im)
l.pack()
canvas=tk.Canvas(root)
canvas.create_image(0,0,anchor='center',image=im)
i=1
def motion(event):
    global i
    x,y = event.x, event.y
    with open("ffaxis.csv",'a') as a:
        filds={'x','y'}
        wr=csv.DictWriter(a,fieldnames=filds)
        wr.writerow({'x':x,'y':y})
        i=i+1
        print(x,y,i)
def delete(event):
    pass
root.bind('<Button-1>',motion)
root.bind('<Button-3>',delete)
root.mainloop()