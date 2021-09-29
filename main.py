from tkinter import *
tk = Tk()
img = Canvas(tk, width=400, height=400)
img.pack()
# img.create_text(150,100, text='Ironman is bad  :)',font=('Times', 15))
# img.create_text(200,200, text='But spider man is better  :D   ')
# img.create_text(200,200, text='But spider man is better  :D   ')
# img.create_text(200,200, text='But spider man is better  :D   ')

img.create_text(150, 150, text='Przybieżeli do Betlejem',
font=('Times', 12))

img.create_text(200, 200, text='Pasterze.',
font=('Times', 18))

img.create_text(200, 240, text='cajac skocznie dzieciate',
font=('Times', 25))


img.create_text(200, 300, text='na lirze."',
font=('Times', 25))


tk.mainloop()

# from tkinter import *
# tk = Tk()
# img = Canvas(tk, width=400, height=400)
# img.pack()
# # img.create_line(0, 0, 500, 500)
# img.create_rectangle(10, 10, 50 ,300)

# def powitanie():
#     print("WHAT UP!")
#
# przycisk = Button(tk, text="kliknij mine", command=powitanie)
# przycisk.pack()
#
#
#
# tk.mainloop()

# def osoba(size, height):
#     print('Mam %s centeretrow szerokosci,%s centeretrow wysokosci' % (size, height))
#
# osoba(height = 30,size = 40)

#
# import turtle
# t = turtle.Turtle()
# list1 = ["Red","Blue","Green","Purple","Orange"]
# for i in range(600):
#     t.color(list1[i % 5])
#     t.pensize(i/10+1)
#     t.forward(i)
#     t.left(59)
#
# turtle.mainloop()




# import tkinter as tk
#
# counter = 0
# def counter_label(label):
#     counter = 0
#     def count():
#         global counter
#         counter += 1
#         label.config(text=str(counter))
#         label.after(10,count)
#     count()
#
# root = tk.Tk()
# root.title("Counter")
# label = tk.Label(root, fg = "Dark Green")
# label.pack()
# counter_label(label)
# button = tk.Button(root,text="stop",width=40,command = root.destroy)
# button.pack()
# root.mainloop()

#
#
# from tkinter import *
# count = 0
#
# def click():
#     global count
#     count += 1
#     print(count)
#

# window = Tk()
# button = Button(window,text='Please Slap Me!')
# button.config(command=click)
# button.config(font=('Ink Free',50,'bold'))
# button.config(bg='#ff6200')
# button.config(fg='#fffb1f')
# button.config(activebackground = '#FF0000')
# button.config(activeforeground = '#fffb1f')
# image = PhotoImage(file='goat.png')
# button.config(image=image)
# button.config(compound='bottom')
# button.pack()
# window.mainloop()





# from tkinter import *
# tk = Tk()
# count = 0
#
# def add():
#     global count
#     count += 1
#     print(count)
#
# def takeaway():
#     global count
#     count -= 1
#     print(count)
#
# button = Button(tk, text ="add", command=add)
# button.pack()
# button2 = Button(tk, text ="takeaway", command=takeaway)
# button2.pack()
#
# tk.mainloop()

from tkinter import *
import random

# tk = Tk()
# img = Canvas(tk, width=400, height=400)
# img.pack()
# def random_rectangle(width, height):
#     x1 = random.randrange(width)
#     y1 = random.randrange(height)
#     x2 = x1 + random.randrange(width)
#     y2 = y1 + random.randrange(height)
#     img.create_rectangle(x1, y1, x2, y2)
#
# def random_squares(width):
#     x1 = random.randrange(width)
#     y1 = x1
#     x2 = x1 + random.randrange(width)
#     y2 = x2
#     img.create_rectangle(x1, y1, x2, y2)
#
# for x in range(0, 100):
#     random_squares(400)

# random_rectangle(400, 400, ’#ffd800 ’)
# random_rectangle(400, 400, ’red ’)
# random_rectangle(400, 400, ’blue ’)
# random_rectangle(400, 400, ’orange ’)
# random_rectangle(400, 400, ’yellow ’)
# random_rectangle(400, 400, ’pink ’)
# random_rectangle(400, 400, ’purple ’)
# random_rectangle(400, 400, ’violet ’)
# random_rectangle(400, 400, ’magenta’)
# random_rectangle(400, 400, ’cyan’)
#
#tk.mainloop()
#
# colorchooser.askcolor()
# from tkinter import colorchooser


# from tkinter import *
# tk = Tk()
# img = Canvas(tk, width=400, height=400)
# img.pack()
# img.create_arc(10, 10, 200, 80, extent=45, style=ARC)
# img.create_arc(10, 80, 200, 160, extent=90, style=ARC)
# img.create_arc(10, 160, 200, 240, extent=135, style=ARC)
# img.create_arc(10, 240, 200, 320, extent=180, style=ARC)
# img.create_arc(10, 320, 200, 400, extent=360, style=ARC)
#
#
#
# tk.mainloop()

#CREATING RECTANGLES
# from tkinter import *
# tk = Tk()
# img = Canvas(tk, width=400, height=400)
# img.pack()
# img.create_rectangle(10, 50,300 ,100)






# from tkinter import *
# tk = Tk()
# img = Canvas(tk, width=400, height=400, color="#26FF00")
# img.pack()
# img.create_rectangle(10, 50,300 ,100,fill="#FF6600")
#
# tk.mainloop()






#
# from tkinter import *
# tk = Tk()
# img = Canvas(tk, width=400, height=400)
# img.pack()
# img.create_rectangle(100, 300,300 ,100)
# img.create_rectangle(45, 234,233 ,89)
# img.create_rectangle(200, 500,200 ,800)
# img.create_rectangle(24, 155,163 ,342)
# img.create_rectangle(765, 423,546 ,243)
# img.create_rectangle(234, 123,100 ,700)
#
# #
# tk.mainloop()

# data = {
#     "ChristianoRonaldo": {
#         "Position": "Striker",
#         "age": "36"
#     }
# }
# n=input('Please enter a players name: ')
#
# if n in data:
#     print(data)

# thisdict = {
# "ChristianoRonaldo": {
#          "Position": "Striker",
#          "age": "36"
#     }
# }
# print(thisdict)


# from tkinter import *
# tk = Tk()
# img = Canvas(tk, width=400, height=400, background="black")
# img.pack()
# tk.mainloop()



# from tkinter import *
# import random
#
# tk = Tk()
# img = Canvas(tk, width=400, height=400)
# img.pack()
#
#
# def random_squares(width):
#     x1 = random.randrange(width)
#     y1 = x1
#     x2 = x1 + random.randrange(width)
#     y2 = x2
#     img.create_rectangle(x1, y1, x2, y2)
#
#
# def random_rectangle(width, height):
#     x1 = random.randrange(width)
#     y1 = random.randrange(height)
#     x2 = x1 + random.randrange(width)
#     y2 = y1 + random.randrange(height)
#     img.create_rectangle(x1, y1, x2, y2)
#
#
#
#
# button = Button(tk, text ="rectangles", command=random_squares(400))
# button.pack()
# button2 = Button(tk, text ="squares", command=random_rectangle(400,400))
# button2.pack()
#
# tk.mainloop()
#







from tkinter import *
#import random

# tk = Tk()
# img = Canvas(tk, width=400, height=400)
# img.pack()
# def random_rectangle(width, height):
#     x1 = random.randrange(width)
#     y1 = random.randrange(height)
#     x2 = x1 + random.randrange(width)
#     y2 = y1 + random.randrange(height)
#     img.create_rectangle(x1, y1, x2, y2)
#
# def random_squares(width):
#     x1 = random.randrange(width)
#     y1 = x1
#     x2 = x1 + random.randrange(width)
#     y2 = x2
#     img.create_rectangle(x1, y1, x2, y2)
#
# for x in range(0, 100):
#     random_squares(400)


