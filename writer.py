from tkinter import *

filename = None

def fNew(*args):
    global filename
    result = messagebox.askyesnocancel("Save file?", "Do you want to save the current file?")
    if(result == True):
        fSave()
    elif(result == None):
        return
    filename = None
    text.delete(0.0, END)
    
def fOpen(*args):
    global filename
    result = messagebox.askyesnocancel("Save file?", "Do you want to save the current file?")
    if(result == True):
        fSave()
    elif(result == None):
        return
    try:
        f = filedialog.askopenfile(filetypes = [('text files', '.txt'),('all files', '.*')])
        if(f):
            filename = f.name
            t = f.read()
            text.delete(0.0, END)
            text.insert(END, t)
    except:
        messagebox.showerror("Error", "Unable to open file.")
      
def fSave(*args):
    global filename
    t = text.get(0.0, END)
    if(filename):
        f = open(filename, "w")
        f.write(t)
        f.close()
    else:
        fSaveAs()

def fSaveAs(*args):
    f = filedialog.asksaveasfile(defaultextension=".txt", filetypes = [('text files', '.txt'),('all files', '.*')])
    t = text.get(0.0, END)
    if(f):
        try:
            f.write(t)
            f.close()
        except:
            messagebox.showwarning("Error", "Unable to save file.")

def onExit(*args):
    result = messagebox.askyesnocancel("Save file?", "Do you want to save the current file?")
    if(result == True):
        fSave()
    elif(result == None):
        return
    writer.destroy()
    
#initialization
writer = Tk()
writer.title("Writer")

#initializing text container
text = Text(writer)

#menu
menubar = Menu(writer)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = fNew)
filemenu.add_command(label = "Open", command = fOpen)
filemenu.add_command(label = "Save", command = fSave)
filemenu.add_command(label = "Save As", command = fSaveAs)
filemenu.add_separator()
filemenu.add_command(label = "About", command = lambda: messagebox.showinfo("About", "A simple text editor made for fun and practice with Python 3.5.2 using the Tkinter module for GUI programming. \nAuthor: Leo Hajder (github.com/lhajder)"))
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = onExit)
menubar.add_cascade(label = "File", menu = filemenu)
writer.config(menu=menubar)

#key Bindings
writer.bind('<Control-n>', fNew)
writer.bind('<Control-o>', fOpen)
writer.bind('<Control-s>', fSave)

#save before exit?
writer.protocol("WM_DELETE_WINDOW", onExit)

#deploying text container
text.pack(expand=True, fill='both')

text.focus()

writer.mainloop()
