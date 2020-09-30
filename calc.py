import tkinter as tk
cal=tk.Tk()
cal.title("Calculator")
variable= tk.StringVar()
display=tk.Entry(cal,font=("arial",20,"bold"),bd=25,textvariable=variable)
display.grid(columnspan=5)
cal.mainloop()


