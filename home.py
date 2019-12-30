from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import  messagebox as mb

def raise_frame(frame):
    frame.tkraise()

win = Tk()
win.title("Account App")
win.geometry('770x490')
# win.resizable(False,False)

s = ttk.Style()
s.configure('Home.TFrame', background='lightblue')
s.configure('Login.TFrame',background="red")

Home = ttk.Frame(win,style='Home.TFrame')
Login = ttk.Frame(win,style='Login.TFrame')
Signup = ttk.Frame(win)

for frames in (Home,Login,Signup):
    frames.grid(row=0,column=0,sticky='news')

"""Home First page"""
app_name = tk.LabelFrame(Home,text="Account App",fg="red",font=('Arial',50),borderwidth=0,labelanchor='n')
app_name.grid(row=0,column=5,padx=145,pady=145,ipadx=50,ipady=50)

text_message = """Welcome To Account App Where you can Store All of your spending"""
app_message = tk.Label(app_name,text=text_message,anchor='center')
app_message.place(x=20,y=20)

home_login_btn = tk.Button(app_name,text="Login",command=lambda:raise_frame(Login))
home_login_btn.place(relx = 0.3, rely = 0.8, anchor = CENTER)

home_signup_btn = tk.Button(app_name,text="Signup",command=lambda :raise_frame(Home))
home_signup_btn.place(relx = 0.6, rely = 0.8, anchor = CENTER)

val = Label(app_name,text="")
val.grid(row=0,column=0)
raise_frame(Login)


"""Login Second Page"""
back_button_login = tk.Button(Login,text="Back",command=lambda : raise_frame(Home))
back_button_login.place(relx = 0.9, rely = 0.0)

label_name = tk.Label(Login,text="Login Window",fg="red",font=('Arial',50),bg='green')
label_name.place(relx = 0.5, rely = 0.2,anchor= CENTER)

email_id = tk.Label(Login,text="Email Id",fg="blue",bg='gray')
email_id.place(relx = 0.35, rely = 0.4,anchor= CENTER)
email_entry = ttk.Entry(Login)
email_entry.place(relx = 0.6, rely = 0.4,anchor= CENTER)

password = tk.Label(Login,text="Password",fg="blue",bg='gray')
password.place(relx = 0.35, rely = 0.5,anchor= CENTER)
password_entry = ttk.Entry(Login)
password_entry.place(relx = 0.6, rely = 0.5,anchor= CENTER)

def submit():
    pass
login_submit_btn = ttk.Button(Login,text="Login",command="pass")
login_submit_btn.place(relx=0.5,rely=0.6,anchor=CENTER)
win.mainloop()