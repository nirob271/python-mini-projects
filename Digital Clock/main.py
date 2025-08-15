import tkinter as tk   # GUI library
from time import strftime

root = tk.Tk()    # main window  
root.title("Digital Clock")

# clock update function
def time():
    string = strftime("%H:%M:%S %p \n %D")
    label.config(text = string)
    label.after(1000,time)
    

# display    
label = tk.Label(root, font=("calibri",50,"bold"),background="yellow",foreground="black") 
label.pack(anchor="center")

time()

root.mainloop()   
