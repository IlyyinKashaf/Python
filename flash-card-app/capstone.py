from tkinter import Tk, Canvas, Button, PhotoImage
from PIL import Image, ImageTk
import pandas 
import random 
BACKGROUND_COLOR = "#B1DDC6"
words = {}
to_learn = {}

#--------------------------------------- french words display ---------------------------------------------#

try:
    data = pandas.read_csv('flash-card-app/data/words_to_learn.csv') 
except FileNotFoundError:
    original_data=pandas.read_csv('flash-card-app/data/french_words.csv')
    to_learn = original_data.to_dict(orient = 'records')
else:
    to_learn = data.to_dict(orient='records')

def next_card ():
    global words,flip_timer
    window.after_cancel(flip_card)
    words = random.choice(to_learn)
    canvas.itemconfig(card_title,text='French',fill='black')
    canvas.itemconfig(card_word,text=words['French'],fill='black')
    canvas.itemconfig(background_image, image = front_image)
    flip_timer=window.after(3000,flip_card)

#----------------------------------------- english word display ---------------------------------------------#
def flip_card():
    canvas.itemconfig(card_title,text='English',fill='white')
    canvas.itemconfig(card_word,text=words['English'],fill='white')
    canvas.itemconfig(background_image,image = back_image)
#---------------------------------------------- right button -----------------------------------------------#
def is_know():
    to_learn.remove(words)
    data = pandas.DataFrame(to_learn)
    data.to_csv("flash-card-app/data/words_to_learn.csv",index=False)
    next_card()
    


#------------------------------------------- UI SETUP --------------------------------------------#

window = Tk()
window.title("Flash Card App")
window.config(padx=20, pady=20,bg=BACKGROUND_COLOR)  



front_image = PhotoImage(file='flash-card-app/images/card_front.png')
canvas = Canvas(width=800, height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
back_image = PhotoImage(file='flash-card-app/images/card_back.png')
background_image = canvas.create_image(400, 263, image=front_image)  
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400,150,text='',font=('ariel',40,'italic'))
card_word=canvas.create_text(400,260,text='',font=('ariel',60,'bold'))

flip_timer = window.after(3000,flip_card)


try:
    
    right_image = PhotoImage(file='flash-card-app/images/right.png')
    wrong_image = PhotoImage(file='flash-card-app/images/wrong.png')
    
    right_button = Button(image=right_image, highlightthickness=0, borderwidth=0 ,command = is_know)
    wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0,command=next_card)
    
    right_button.grid(row=1, column=1, pady=(10, 0))  # Small top padding
    wrong_button.grid(row=1, column=0, pady=(10, 0))
    
except Exception as e:
    print(f"Error loading images: {e}")


next_card()

window.mainloop()


    
   
    
