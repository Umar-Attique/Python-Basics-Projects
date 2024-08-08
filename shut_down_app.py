from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")



import tkinter as tk  # Make sure to import tkinter

st = tk.Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg='Blue')

r_button = tk.Button(st, text='Restart', font=('Times New Roman', 20, 'bold'), relief='raised', cursor='plus',command=restart)
r_button.place(x=150, y=60, height=50, width=200)

r_button = tk.Button(st, text='Restart Time', font=('Times New Roman',20, 'bold'), relief='raised', cursor='plus',command=restart_time)
r_button.place(x=150, y=170, height=50, width=200)

lg_button = tk.Button(st, text='Log-Out', font=('Times New Roman',20, 'bold'), relief='raised', cursor='plus',command=log_out)
lg_button.place(x=150, y=270, height=50, width=200)

st_button = tk.Button(st, text='Shutdown', font=('Times New Roman',20, 'bold'), relief='raised', cursor='plus',command=shutdown)
st_button.place(x=150, y=370, height=50, width=200)

st.mainloop()
