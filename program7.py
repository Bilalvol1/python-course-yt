import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

# main loop
while run:
    root = Tk()
    root.geometry('905x700')
    root.title('HANG MAN')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0

    # choosing word
    index = random.randint(0,853)
    file = open('words.txt','r')
    l = file.readlines()
    selected_word = l[index].strip('\n')
    
    # creation of word dashes variables
    x = 250
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))
        
    #letters icon
    al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let,let))
        
    # hangman images