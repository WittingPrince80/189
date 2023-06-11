import hashlib 
from tkinter import *
from firebase import firebase

registration_window = Tk()
registration_window.geometry("400x400")

def firebase.FirebaseApplication( ):
    database link
     Authentication= "None"
     background.config(black)
     login_username_entry = ""
    
def login(): 
    print("login function")
    username = login_username_entry.get()
    password = login_password_entry.get()
    
    print("MD5 function")
    text_file = fd.askopenfilename(title=" Open Text File", filetypes=(("Text Files", ".txt"),))
    print(text_file)
    read_file = open(text_file,'r')
    paragraph=read_file.read()
    file_result = hashlib.md5(paragraph.encode())
    file_hexd = file_result.hexdigest()
    print(file_hexd)
    md5_file = open("md5.*txt",'w')
    md5_file.write(file_hexd)
    print(file_hexd)
    
    md5_file.close
    print(password)
    
    if get_password = hexadecimal_password:
        print("Succesfully Loggedin")
def register(): 
    print("register function")
   username = registration_window.get(username)
   password = registration_window.get(password)
   passcode = md5(password)
   passcode.hexdigest() = encryptedcode
   firebase.put()
def login_window():
    global login_username_entry
    global login_password_entry
    registration_window.destroy()
    login_window.config()
    login_window = Tk()
    login_window.geometry("400x400")
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold')
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13')
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13')
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT)
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold')
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13')
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13')
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10)
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT)

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()