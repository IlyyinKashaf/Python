import random 
from random import choice,randint,shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letter = [choice(letters) for _ in range(randint(8, 10))]
        passord_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        password_symbols  = [choice(symbols) for _ in range(randint(2, 4))]
        password_list = password_letter+passord_numbers + password_symbols

        random.shuffle(password_list)

        password = "".join(password_list)
        password_entry.insert(0,password)
        pyperclip.copy(password)


        

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    
    website = website_entry.get()
    email = name_entry.get()
    password = password_entry.get()
    if len(website) ==0 or len(email)==0 or len(password) ==0:
        messagebox.showinfo("Oops! you have left empty")
    

    else:
        write_data=f"Website: {website}\nEmail: {email}\nPassword: {password}\n"
        is_ok = messagebox.askokcancel(title='website',message=write_data )
        if is_ok:
            with open('password-manager/demo.txt','a') as file:
                file.write(write_data)
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                       


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=224, highlightthickness=0)
lock_img = PhotoImage(file="password-manager/logo.png")  # Update path if needed
canvas.create_image(100, 112, image=lock_img)
canvas.grid(column=1,row=0)

website_label= Label(text='Website:',fg= 'black',font='Calibri')
website_label.grid(column = 0,row=1)
website_entry = Entry(window,width=65)
website_entry.grid(row=1,column=1 ,columnspan= 2)

name_label= Label(text='Email/Username:',fg= 'black',font='Calibri')
name_label.grid(column = 0,row=2)
name_entry = Entry(window,width=65)
name_entry.grid(row=2,column=1 ,columnspan= 2)
name_entry.insert(0,'ilyyinkashaf4@gmail.com')

password_label= Label(text='Password:',fg= 'black',font='Calibri')
password_label.grid(column = 0,row=3)
password_entry = Entry(window,width=33)
password_entry.grid(row=3,column=1)

generate_button = Button(text='Generate Password',width=25,command=password_generator)
generate_button.grid(row =3 , column = 2)
add_button = Button(text='Add',width = 55,command=get_data)
add_button.grid(row=4,column=1,columnspan=2)








window.mainloop()
