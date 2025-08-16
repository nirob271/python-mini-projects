import tkinter as tk


root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x200")
root.resizable(False, False)


time_left = 0


def start_countdown():
    global time_left
    try:
        time_left = int(entry.get())
        countdown()
    except ValueError:
        label.config(text="Enter a number")    
        
    



def countdown():
    global time_left
    if time_left>=0:
        label.config(text = str(time_left))
        time_left -= 1
        label.after(1000,countdown)
    else:
        label.config(text="Time is up!")


entry = tk.Entry(root,font=("Times New Roman",20),justify="center")
entry.pack(pady=10)


start_button = tk.Button(root, text="Start Countdown", font=("Times New Roman", 16), command=start_countdown)
start_button.pack(pady=5)


label = tk.Label(root,font=("Times New Roman",50,"bold"),background=("white"),foreground="black")
label.pack(anchor="center")


countdown()

root.mainloop()            