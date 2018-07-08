from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

add = os.getcwd()

root = Tk()

#setting up a tkinter canvas with scrollbars
frame = Frame(root, bd=2, relief=SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
xscroll = Scrollbar(frame, orient=HORIZONTAL)
xscroll.grid(row=1, column=0, sticky=E+W)
yscroll = Scrollbar(frame)
yscroll.grid(row=0, column=1, sticky=N+S)
canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
xscroll.config(command=canvas.xview)
yscroll.config(command=canvas.yview)
frame.pack(fill=BOTH,expand=1)

imlist = [ [None] * 16 for i in range(51) ]
for i in range(1,51):
    for j in (1,2,3,4,6,7,8,10,11,12,13,14,15):
        if (i < 10):
            if(j < 10):
                imlist[i][j] = Image.open('Face Database/'+'s0'+str(i)+'_0'+str(j)+'.jpg')
            else:
                imlist[i][j] = Image.open('Face Database/'+'s0'+str(i)+'_'+str(j)+'.jpg')
        else:
            if(j < 10):
                imlist[i][j] = Image.open('Face Database/'+'s'+str(i)+'_0'+str(j)+'.jpg')
            else:
                imlist[i][j] = Image.open('Face Database/'+'s'+str(i)+'_'+str(j)+'.jpg')
#imlist[50][15].show()

#function to be called when mouse is clicked

def printcoords():
    File = filedialog.askopenfilename(parent=root, initialdir=add,title='Choose an image.')
    filename = ImageTk.PhotoImage(Image.open(File))
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)

def train():
    pass
    
    
    
def test():
    pass
    
    
    
    
Button(root,text='choose',command=printcoords).pack()
Button(root,text='train',command=train).pack()
Button(root,text='test',command=test).pack()

print('XD')
root.mainloop()
print('XD')
