import db_code
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import  messagebox as m_box

def raise_frame(frame):
    frame.tkraise()

win = Tk()
win.title("Account App")
win.geometry('770x490')
win.resizable(False,False)

s = ttk.Style()
s.configure('Home.TFrame', background='lightblue')
s.configure('Login.TFrame',background="lightblue")
s.configure('Signup.TFrame',background="lightblue")

Home = ttk.Frame(win,style='Home.TFrame')
Login = ttk.Frame(win,style='Login.TFrame')
Signup = ttk.Frame(win,style='Signup.TFrame')

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

home_signup_btn = tk.Button(app_name,text="Signup",command=lambda :raise_frame(Signup))
home_signup_btn.place(relx = 0.6, rely = 0.8, anchor = CENTER)

val = Label(app_name,text="")
val.grid(row=0,column=0)



"""Login Second Page"""
back_button_login = tk.Button(Login,text="Back",command=lambda : raise_frame(Home))
back_button_login.place(relx = 0.9, rely = 0.0)

label_name_login = tk.Label(Login,text="Login Window",fg="red",font=('Arial',50))
label_name_login.place(relx = 0.5, rely = 0.2,anchor= CENTER)

email_id = tk.Label(Login,text="Email Id",fg="blue")
email_id.place(relx = 0.35, rely = 0.4,anchor= CENTER)
email_entry = ttk.Entry(Login)
email_entry.place(relx = 0.6, rely = 0.4,anchor= CENTER)

password = tk.Label(Login,text="Password",fg="blue")
password.place(relx = 0.35, rely = 0.5,anchor= CENTER)
password_entry = ttk.Entry(Login)
password_entry.place(relx = 0.6, rely = 0.5,anchor= CENTER)

def submit():
    pass
login_submit_btn = ttk.Button(Login,text="Login",command="pass")
login_submit_btn.place(relx=0.5,rely=0.6,anchor=CENTER)

"""SignUp Third Page"""
back_button_signup = tk.Button(Signup,text="Back",command=lambda : raise_frame(Home))
back_button_signup.place(relx = 0.9, rely = 0.0)

label_name_signup = tk.Label(Signup,text="Sign Up Window",fg="red",font=('Arial',50))
label_name_signup.place(relx = 0.5, rely = 0.2,anchor= CENTER)

signup_name = tk.Label(Signup,text="Name",fg="blue")
signup_name.place(relx = 0.35, rely = 0.35,anchor= CENTER)
signup_name_entry = ttk.Entry(Signup)
signup_name_entry.place(relx = 0.55, rely = 0.35,anchor= CENTER)

signup_dob = tk.Label(Signup,text="DOB",fg="blue")
signup_dob.place(relx = 0.35, rely = 0.4,anchor= CENTER)
signup_dob_entry = ttk.Entry(Signup)
signup_dob_entry.place(relx = 0.55, rely = 0.4,anchor= CENTER)

# DOB BUTTON


def DOB():
    from tkcalendar import Calendar
    def print_sel():
        # print(cal.selection_get())
        signup_dob_entry.delete(0,END)
        signup_dob_entry.insert(0,cal.selection_get())
        top.destroy()

    top = tk.Toplevel(win)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

signup_dob_button = ttk.Button(Signup,text="DOB",command=DOB)
signup_dob_button.place(relx=0.72,rely=0.4,anchor=CENTER)

signup_mobno = tk.Label(Signup,text="Mob_No",fg="blue")
signup_mobno.place(relx = 0.35, rely = 0.45,anchor= CENTER)
signup_mobno_entry = ttk.Entry(Signup)
signup_mobno_entry.place(relx = 0.55, rely = 0.45,anchor= CENTER)

signup_email_id = tk.Label(Signup,text="Email ID",fg="blue")
signup_email_id.place(relx = 0.35, rely = 0.5,anchor= CENTER)
signup_email_entry = ttk.Entry(Signup)
signup_email_entry.place(relx = 0.55, rely = 0.5,anchor= CENTER)

signup_password = tk.Label(Signup,text="Password",fg="blue")
signup_password.place(relx = 0.35, rely = 0.55,anchor= CENTER)
signup_password_entry = ttk.Entry(Signup)
signup_password_entry.place(relx = 0.55, rely = 0.55,anchor= CENTER)

signup_Cpassword = tk.Label(Signup,text="Confirm Password",fg="blue")
signup_Cpassword.place(relx = 0.35, rely = 0.6,anchor= CENTER)
signup_Cpassword_entry = ttk.Entry(Signup)
signup_Cpassword_entry.place(relx = 0.55, rely = 0.6,anchor= CENTER)

signuup_profilePhoto = tk.Label(Signup,text="Profile-Photo",fg="blue")
signuup_profilePhoto.place(relx = 0.35, rely = 0.65,anchor= CENTER)
signuup_profilePhoto_entry = Text(Signup,width=30,height=1)
signuup_profilePhoto_entry.place(relx = 0.6, rely = 0.65,anchor= CENTER)

# Profile Photo BUTTON
def profilePhoto():
    pass
signuup_profilePhoto_upload = ttk.Button(Signup,text="Upload")
signuup_profilePhoto_upload.place(relx=0.82,rely=0.65,anchor=CENTER)

signup_register = ttk.Button(Signup,text="Register",command=lambda : raise_frame(Login))
signup_register.place(relx=0.45,rely=0.75,anchor=CENTER)

raise_frame(Home)
win.mainloop()
