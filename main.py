from tkinter import *
from tkinter import ttk
from random import randint
import time

# global variable
score = 0
bananas = None
text = None

# Creating the Canvas
screen = Tk()
width = 500
height = 500
canvas = Canvas(width=width,height=height,highlightthickness=0)
canvas.pack()

# Drawing a background Image
img = PhotoImage(file='background.gif')
w = img.height()
h = img.width()
# print(w,h) 
for x in range(6):
    for y in range(6):
        canvas.create_image(x*w,y*h,image=img)
# writing the initial text
text = canvas.create_text(250,250,text=f'{score}',fill='white',font=('Helvetica 40 bold'))
    

# creating the banana
banana_img = PhotoImage(file='banimg.gif')
# wi = banana_img.width()
# hi = banana_img.height()
# print(hi,wi)

# increasing the score when the user click a banana and 
# deleting the previous banana
def increase_score(e):
    global score, text
    score += 1
    canvas.delete(text)
    text = canvas.create_text(250,250,text=f'{score}',fill='white',font=('Helvetica 40 bold'))

# placing the banana on the screen and repeating the process
def bring_banana():
    global bananas
    canvas.delete(bananas)
    bananas = canvas.create_image(randint(25,460),randint(25,460),image=banana_img)
    canvas.tag_bind(bananas, '<Button-1>', increase_score)
    
    #bring the image again 
    screen.after(1000,bring_banana)

# calling the initial banana function
bring_banana()

# ensures the screen is always listening 
screen.mainloop()
