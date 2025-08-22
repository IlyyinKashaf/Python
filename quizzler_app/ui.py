from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain):
        self_quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.label = Label(text='Score: 0',bg=THEME_COLOR)
        self.label.grid(column=1,row=0)

        
        
        self.canvas = Canvas(width = 300,height=250,bg='white')
        self.question_text = self.canvas.create_text(150, 125, text="Some question", font=("Arial", 12, "bold"),)
        self.canvas.grid(column=0,row=1,columnspan=2)
       
        self.right_image = PhotoImage(file='quizzler_app/images/true.png')
        self.right_button = Button(image = self.right_image)
        self.right_button.grid(padx=20,pady=20,column=0,row=2)
        self.false_image = PhotoImage(file='quizzler_app/images/false.png')
        self.false_button = Button(image = self.false_image)
        self.false_button.grid(padx=20,pady=20,column=1,row=2)
    
    def get_next_question():


        



        self.window.mainloop()
    

