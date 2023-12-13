import tkinter as tk
from tkinter import ttk

# functions 

exp = " "

def press(key):
    global exp
    exp += key
    textPanel.set(exp)


def clear():
    global exp
    exp = " " 
    textPanel.set(exp)

def esc():
    pass

def caps():
    pass

def enter():
    global exp
    exp += "\n"
    textPanel.set(exp) 

def shift():
    pass

def control():
    pass

def win():
    pass

def alt():
    pass

def opt():
    pass


def back():
    global exp
    exp = exp[0:-1]
    textPanel.set(exp)


# window start

keyboard = tk.Tk()
winWidth=1080
winHeight=550
keyboard.maxsize(winWidth,winHeight)
keyboard.minsize(winWidth,winHeight)
keyboard.iconbitmap('keyboard.ico')
keyboard.title('Keyboard by Mohit')
keyboard.config(bg='lightgrey')

textPanel = tk.StringVar()
textArea = tk.Label(keyboard, height=12, textvariable = textPanel, bg='white')
textArea.pack(fill='x')

# number row

numberRow = tk.Label(keyboard)
numberRow.pack()

# number row keys

ttk.Button(numberRow, text='~', command=lambda: press('~'), style="big.TButton", width=8).grid(row=0, column=0, padx=2, ipady=20)
ttk.Button(numberRow, text='1', command=lambda: press('1'), style="big.TButton", width=8).grid(row=0, column=1, padx=2, ipady=20)
ttk.Button(numberRow, text='2', command=lambda: press('2'), style="big.TButton", width=8).grid(row=0, column=2, padx=2, ipady=20)
ttk.Button(numberRow, text='3', command=lambda: press('3'), style="big.TButton", width=8).grid(row=0, column=3, padx=2, ipady=20)
ttk.Button(numberRow, text='4', command=lambda: press('4'), style="big.TButton", width=8).grid(row=0, column=4, padx=2, ipady=20)
ttk.Button(numberRow, text='5', command=lambda: press('5'), style="big.TButton", width=8).grid(row=0, column=5, padx=2, ipady=20)
ttk.Button(numberRow, text='6', command=lambda: press('6'), style="big.TButton", width=8).grid(row=0, column=6, padx=2, ipady=20)
ttk.Button(numberRow, text='7', command=lambda: press('7'), style="big.TButton", width=8).grid(row=0, column=7, padx=2, ipady=20)
ttk.Button(numberRow, text='8', command=lambda: press('8'), style="big.TButton", width=8).grid(row=0, column=8, padx=2, ipady=20)
ttk.Button(numberRow, text='9', command=lambda: press('9'), style="big.TButton", width=8).grid(row=0, column=9, padx=2, ipady=20)
ttk.Button(numberRow, text='0', command=lambda: press('0'), style="big.TButton", width=8).grid(row=0, column=10, padx=2, ipady=20)
ttk.Button(numberRow, text='-', command=lambda: press('-'), style="big.TButton", width=8).grid(row=0, column=11, padx=2, ipady=20)
ttk.Button(numberRow, text='+', command=lambda: press('+'), style="big.TButton", width=8).grid(row=0, column=12, padx=2, ipady=20)
ttk.Button(numberRow, text='Bks', command=back, style="big.TButton", width=21).grid(row=0, column=13, padx=2, ipady=20)

# first row

firstRow = tk.Label(keyboard)
firstRow.pack()

# first row keys

ttk.Button(firstRow, text='Tab', command=lambda: press('    '), style="big.TButton").grid(row=0, column=0, padx=2, ipadx=7, ipady=20)
ttk.Button(firstRow, text='Q', command=lambda: press('Q'), style="big.TButton", width=8).grid(row=0, column=1, padx=2, ipady=20)
ttk.Button(firstRow, text='W', command=lambda: press('W'), style="big.TButton", width=8).grid(row=0, column=2, padx=2, ipady=20)
ttk.Button(firstRow, text='E', command=lambda: press('E'), style="big.TButton", width=8).grid(row=0, column=3, padx=2, ipady=20)
ttk.Button(firstRow, text='R', command=lambda: press('R'), style="big.TButton", width=8).grid(row=0, column=4, padx=2, ipady=20)
ttk.Button(firstRow, text='T', command=lambda: press('T'), style="big.TButton", width=8).grid(row=0, column=5, padx=2, ipady=20)
ttk.Button(firstRow, text='Y', command=lambda: press('Y'), style="big.TButton", width=8).grid(row=0, column=6, padx=2, ipady=20)
ttk.Button(firstRow, text='U', command=lambda: press('U'), style="big.TButton", width=8).grid(row=0, column=7, padx=2, ipady=20)
ttk.Button(firstRow, text='I', command=lambda: press('I'), style="big.TButton", width=8).grid(row=0, column=8, padx=2, ipady=20)
ttk.Button(firstRow, text='O', command=lambda: press('O'), style="big.TButton", width=8).grid(row=0, column=9, padx=2, ipady=20)
ttk.Button(firstRow, text='P', command=lambda: press('P'), style="big.TButton", width=8).grid(row=0, column=10, padx=2, ipady=20)
ttk.Button(firstRow, text='{', command=lambda: press('{'), style="big.TButton", width=8).grid(row=0, column=11, padx=2, ipady=20)
ttk.Button(firstRow, text='}', command=lambda: press('}'), style="big.TButton", width=8).grid(row=0, column=12, padx=2, ipady=20)
ttk.Button(firstRow, text='Clear', command=clear).grid(row=0, column=13, padx=2, ipadx=24, ipady=20)

mergeRow = tk.Frame(keyboard)
mergeRow.pack()

# enter section

enterSection = tk.Label(mergeRow)
ttk.Button(enterSection, text='Enter', command=enter, style='big.TButton').grid(ipadx=9, ipady=55)
enterSection.grid(rowspan=2, column=1)

# second row 

secondRow = tk.Label(mergeRow)
secondRow.grid(row=0, column=0)

# second row keys

ttk.Button(secondRow, text='Caps', command=caps, style="big.TButton").grid(row=0, column=0, padx=2, ipadx=15, ipady=20)
ttk.Button(secondRow, text='A', command=lambda: press('A'), style="big.TButton", width=8).grid(row=0, column=1, padx=2, ipady=20)
ttk.Button(secondRow, text='S', command=lambda: press('S'), style="big.TButton", width=8).grid(row=0, column=2, padx=2, ipady=20)
ttk.Button(secondRow, text='D', command=lambda: press('D'), style="big.TButton", width=8).grid(row=0, column=3, padx=2, ipady=20)
ttk.Button(secondRow, text='F', command=lambda: press('F'), style="big.TButton", width=8).grid(row=0, column=4, padx=2, ipady=20)
ttk.Button(secondRow, text='G', command=lambda: press('G'), style="big.TButton", width=8).grid(row=0, column=5, padx=2, ipady=20)
ttk.Button(secondRow, text='H', command=lambda: press('H'), style="big.TButton", width=8).grid(row=0, column=6, padx=2, ipady=20)
ttk.Button(secondRow, text='J', command=lambda: press('J'), style="big.TButton", width=8).grid(row=0, column=7, padx=2, ipady=20)
ttk.Button(secondRow, text='K', command=lambda: press('K'), style="big.TButton", width=8).grid(row=0, column=8, padx=2, ipady=20)
ttk.Button(secondRow, text='L', command=lambda: press('L'), style="big.TButton", width=8).grid(row=0, column=9, padx=2, ipady=20)
ttk.Button(secondRow, text=':', command=lambda: press(':'), style="big.TButton", width=8).grid(row=0, column=10, padx=2, ipady=20)
ttk.Button(secondRow, text='"', command=lambda: press('"'), style="big.TButton", width=8).grid(row=0, column=11, padx=2, ipady=20)
ttk.Button(secondRow, text='|', command=lambda: press('|'), style="big.TButton", width=8).grid(row=0, column=12, padx=2, ipady=20)

# third row

thirdRow = tk.Label(mergeRow)
thirdRow.grid(row=1, column=0)
ttk.Button(thirdRow, text='Shift', command=shift, style="big.TButton").grid(row=0, column=0, padx=2, ipadx=20, ipady=20)
ttk.Button(thirdRow, text='Z', command=lambda: press('Z'), style="big.TButton", width=8).grid(row=0, column=1, padx=2, ipady=20)
ttk.Button(thirdRow, text='X', command=lambda: press('X'), style="big.TButton", width=8).grid(row=0, column=2, padx=2, ipady=20)
ttk.Button(thirdRow, text='C', command=lambda: press('C'), style="big.TButton", width=8).grid(row=0, column=3, padx=2, ipady=20)
ttk.Button(thirdRow, text='V', command=lambda: press('V'), style="big.TButton", width=8).grid(row=0, column=4, padx=2, ipady=20)
ttk.Button(thirdRow, text='B', command=lambda: press('B'), style="big.TButton", width=8).grid(row=0, column=5, padx=2, ipady=20)
ttk.Button(thirdRow, text='N', command=lambda: press('N'), style="big.TButton", width=8).grid(row=0, column=6, padx=2, ipady=20)
ttk.Button(thirdRow, text='M', command=lambda: press('M'), style="big.TButton", width=8).grid(row=0, column=7, padx=2, ipady=20)
ttk.Button(thirdRow, text='<', command=lambda: press('<'), style="big.TButton", width=8).grid(row=0, column=8, padx=2, ipady=20)
ttk.Button(thirdRow, text='>', command=lambda: press('>'), style="big.TButton", width=8).grid(row=0, column=9, padx=2, ipady=20)
ttk.Button(thirdRow, text='?', command=lambda: press('?'), style="big.TButton", width=8).grid(row=0, column=10, padx=2, ipady=20)
ttk.Button(thirdRow, text='Shift', command=shift, style="big.TButton").grid(row=0, column=11, padx=2,ipadx=20, ipady=20)

# fourth row

fourthRow = tk.Label(keyboard)
fourthRow.pack()

# fourth row keys

ttk.Button(fourthRow, text='Ctrl', style='big.TButton', command=control, width=10).grid(row=0, column=0, ipady=20)
ttk.Button(fourthRow, text='Win', style='big.TButton', command=win, width=10).grid(row=0, column=1, ipady=20)
ttk.Button(fourthRow, text='Alt', style='big.TButton', command=alt, width=10).grid(row=0, column=2, ipady=20)
ttk.Button(fourthRow, text=' ', style='big.TButton', command=lambda: press(' '), width=10).grid(row=0, column=3, ipadx=215, ipady=20)
ttk.Button(fourthRow, text='Alt', style='big.TButton', command=alt, width=10).grid(row=0, column=4, ipady=20)
ttk.Button(fourthRow, text='Win', style='big.TButton', command=win, width=10).grid(row=0, column=5, ipady=20)
ttk.Button(fourthRow, text='Opt', style='big.TButton', command=opt, width=10).grid(row=0, column=6, ipadx=2, ipady=20)
ttk.Button(fourthRow, text='Ctrl', style='big.TButton', command=control, width=10).grid(row=0, column=7, ipady=20)

ttk.Style().configure('big.TButton', font=(None, 10))

keyboard.mainloop()

