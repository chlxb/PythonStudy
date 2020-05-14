
''' 
    如果导入 tkinter 运行报错： import _tkinter # If this fails your Python may not be configured for Tk，
    sudo pacman -S tk 
'''
from tkinter import Tk, Button, mainloop

top = Tk()
mainloop()
btn = Button()
btn.pack()
btn['text'] = 'Click me!'
btn['command'] = clicked

def clicked():
    print('I was clicked!')


