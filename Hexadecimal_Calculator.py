from tkinter import *
from tkinter.messagebox import *
import re

window = Tk()
window.title("Hex Calculator")
window.geometry('240x400')

font = ('Verdana', 18)


def btnClick(event):
    b = event.widget
    text = b['text']
    if text == '+':
        textField.insert(END, '+')
        return
    if text == '-':
        textField.insert(END, '-')
        return
    if text == 'x':
        textField.insert(END, '*')
        return
    if text == '/':
        textField.insert(END, '/')
        return
    if text == '=':
        try:
            ex = textField.get()
            if '+' in ex:
                res = re.split("\+", ex)
                first = res[:1]
                second = res[1:]
                num1 = first[0]
                num2 = second[0]
                sum = hex(int(num1, 16) + int(num2, 16))
                textField.delete(0, END)
                textField.insert(0, sum)

            elif '-' in ex:
                res = re.split(" \- ", ex)
                first = res[:1]
                second = res[1:]
                num1 = first[0]
                num2 = second[0]
                min = hex(int(num1, 16) - int(num2, 16))
                textField.delete(0, END)
                textField.insert(0, min)

            elif '*' in ex:
                res = re.split("\*", ex)
                first = res[:1]
                second = res[1:]
                num1 = first[0]
                num2 = second[0]
                multi = hex(int(num1, 16) * int(num2, 16))
                textField.delete(0, END)
                textField.insert(0, multi)
                print("The multiplication is", multi)
            elif "/" in ex:
                res = re.split("\/", ex)
                first = res[:1]
                second = res[1:]
                num1 = first[0]
                num2 = second[0]
                divide = hex(int(num1, 16) // int(num2, 16))
                textField.delete(0, END)
                textField.insert(0, divide)
                print("The divide is ", divide)

        except Exception as e:
            showerror("Error", e)
            return
            textField.insert(END, text)
    try:
        if text != "=":
            hexnum = text
            textField.insert(END, hexnum)
    except Exception as e:
        showerror("Error", e)
        return

def clearall():
    textField.delete(0, END)


def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


textField = Entry(window, font=('Verdana', 22), justify=CENTER, relief=RIDGE, bg='lightgray')
textField.pack(side=TOP, pady=5, fill=X, padx=5, ipady=10)
btnFrame = Frame(window)
btnFrame.pack(side=TOP)
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn1 = Button(btnFrame, text=str(temp), font=font, width=3, relief='ridge', activebackground='black',
                      activeforeground='white', bg='whitesmoke')
        btn1.grid(row=i, column=j)
        temp = temp + 1
        btn1.bind('<Button-1>', btnClick)

zeroBtn = Button(btnFrame, text="0", font=font, width=3, relief='ridge', activebackground='black',
                 activeforeground='white', bg='whitesmoke')
zeroBtn.grid(row=3, column=0)
zeroBtn.bind('<Button-1>', btnClick)

fBtn = Button(btnFrame, text="F", font=font, width=3, relief='ridge', activebackground='black', bg='whitesmoke',
              activeforeground='white')
fBtn.grid(row=3, column=1)
fBtn.bind('<Button-1>', btnClick)

eBtn = Button(btnFrame, text="E", font=font, width=3, relief='ridge', activebackground='black', bg='whitesmoke',
              activeforeground='white')
eBtn.grid(row=3, column=2)
eBtn.bind('<Button-1>', btnClick)

aBtn = Button(btnFrame, text="A", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
              activeforeground='white')
aBtn.grid(row=0, column=3)
aBtn.bind('<Button-1>', btnClick)

bBtn = Button(btnFrame, text="B", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
              activeforeground='white')
bBtn.grid(row=1, column=3)
bBtn.bind('<Button-1>', btnClick)

cBtn = Button(btnFrame, text="C", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
              activeforeground='white')
cBtn.grid(row=2, column=3)
cBtn.bind('<Button-1>', btnClick)

dBtn = Button(btnFrame, text="D", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
              activeforeground='white')
dBtn.grid(row=3, column=3)
dBtn.bind('<Button-1>', btnClick)

plusBtn = Button(btnFrame, text="+", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
                 activeforeground='white')
plusBtn.grid(row=5, column=1)
plusBtn.bind('<Button-1>', btnClick)

minBtn = Button(btnFrame, text="-", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
                activeforeground='white')
minBtn.grid(row=5, column=0)
minBtn.bind('<Button-1>', btnClick)

mutipliBtn = Button(btnFrame, text="x", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
                    activeforeground='white')
mutipliBtn.grid(row=5, column=2)
mutipliBtn.bind('<Button-1>', btnClick)

divideBtn = Button(btnFrame, text="/", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
                   activeforeground='white')
divideBtn.grid(row=5, column=3)
divideBtn.bind('<Button-1>', btnClick)

clearBtn = Button(btnFrame, text="->", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
                  activeforeground='white', command=clear)
clearBtn.grid(row=6, column=1)

clearallBtn = Button(btnFrame, text="AC", font=font, width=3, relief='ridge', activebackground='black', bg='gainsboro',
                     activeforeground='white', command=clearall)
clearallBtn.grid(row=6, column=0)

clearBtn = Button(btnFrame, text="=", font=font, width=7, relief='ridge', activebackground='black', bg='gainsboro',
                  activeforeground='white')
clearBtn.grid(row=6, column=2, columnspan=2)
clearBtn.bind('<Button-1>', btnClick)
window.mainloop()