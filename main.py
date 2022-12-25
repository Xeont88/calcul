from tkinter import *
from tkinter import ttk

a = 0
b = 0
last_action = ''
is_new_number = True


def set_text(num):
    global is_new_number

    temp = text_space.cget("text")
    if temp != '0' and not is_new_number:
        text_space.config(text=temp + num)
    else:
        text_space.config(text=num)
        is_new_number = False


def action(sign):
    global a
    global last_action
    global is_new_number

    if sign != '=':
        a = text_space.cget('text')
        last_action = sign
        is_new_number = True
    else:
        if last_action == "+":
            text_space.config(text=str(float(a) + float(text_space.cget('text'))))
        if last_action == "-":
            text_space.config(text=str(float(a) - float(text_space.cget('text'))))
        if last_action == "*":
            text_space.config(text=str(float(a) * float(text_space.cget('text'))))
        if last_action == "/":
            text_space.config(text=str(float(a) / float(text_space.cget('text'))))


def minus_sign_func():
    n = text_space.cget('text')
    n = -float(n)
    text_space.config(text=n)


def backspace():
    n = text_space.cget('text')
    if len(n) > 1:
        n = n[:-1]
    else:
        n = '0'
    text_space.config(text=n)


def clear():
    text_space.config(text='0')


root = Tk()
root.title('Calc tkinter ver')
root.geometry('300x350+500+200')

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 16), background="#000000")

text_space = Label(text='0', font='Arial 24', anchor=E)
text_space.place(relx=0, rely=0,
                 relwidth=1, relheight=0.2)

btn_frame = ttk.Frame(relief=GROOVE, )
btn_frame.place(relx=0, rely=0.2,
                relwidth=1, relheight=0.8)

CE_btn = ttk.Button(btn_frame, text='CE', command=clear)
CE_btn.place(relx=0, rely=0.0,
             relwidth=0.25, relheight=0.2)

C_btn = ttk.Button(btn_frame, text='C', command=clear)
C_btn.place(relx=0.25, rely=0.0,
            relwidth=0.25, relheight=0.2)

BS_btn = ttk.Button(btn_frame, text='BS', command=backspace)
BS_btn.place(relx=0.5, rely=0.0,
             relwidth=0.25, relheight=0.2)

div_btn = ttk.Button(btn_frame, text='/', style='my.TButton',
                     command=lambda: action('/'))
div_btn.place(relx=0.75, rely=0.0,
              relwidth=0.25, relheight=0.2)

n7_btn = ttk.Button(btn_frame, text='7', style='my.TButton',
                    command=lambda: set_text('7'))
n7_btn.place(relx=0.0, rely=0.2,
             relwidth=0.25, relheight=0.2)

n8_btn = ttk.Button(btn_frame, text='8', style='my.TButton',
                    command=lambda: set_text('8'))
n8_btn.place(relx=0.25, rely=0.2,
             relwidth=0.25, relheight=0.2)

n9_btn = ttk.Button(btn_frame, text='9', style='my.TButton',
                    command=lambda: set_text('9'))
n9_btn.place(relx=0.5, rely=0.2,
             relwidth=0.25, relheight=0.2)

mul_btn = ttk.Button(btn_frame, text='*', style='my.TButton',
                     command=lambda: action('*'))
mul_btn.place(relx=0.75, rely=0.2,
              relwidth=0.25, relheight=0.2)

n4_btn = ttk.Button(btn_frame, text='4', style='my.TButton',
                    command=lambda: set_text('4'))
n4_btn.place(relx=0.0, rely=0.4,
             relwidth=0.25, relheight=0.2)

n5_btn = ttk.Button(btn_frame, text='5', style='my.TButton',
                    command=lambda: set_text('5'))
n5_btn.place(relx=0.25, rely=0.4,
             relwidth=0.25, relheight=0.2)

n6_btn = ttk.Button(btn_frame, text='6', style='my.TButton',
                    command=lambda: set_text('6'))
n6_btn.place(relx=0.5, rely=0.4,
             relwidth=0.25, relheight=0.2)

plus_btn = ttk.Button(btn_frame, text='+', style='my.TButton',
                      command=lambda: action('+'))
plus_btn.place(relx=0.75, rely=0.4,
               relwidth=0.25, relheight=0.2)

n1_btn = ttk.Button(btn_frame, text='1', style='my.TButton',
                    command=lambda: set_text('1'))
n1_btn.place(relx=0.0, rely=0.6,
             relwidth=0.25, relheight=0.2)

n2_btn = ttk.Button(btn_frame, text='2', style='my.TButton',
                    command=lambda: set_text('2'))
n2_btn.place(relx=0.25, rely=0.6,
             relwidth=0.25, relheight=0.2)

n3_btn = ttk.Button(btn_frame, text='3', style='my.TButton',
                    command=lambda: set_text('3'))
n3_btn.place(relx=0.5, rely=0.6,
             relwidth=0.25, relheight=0.2)

equal_btn = ttk.Button(btn_frame, text='-', style='my.TButton',
                       command=lambda: action('-'))
equal_btn.place(relx=0.75, rely=0.6,
                relwidth=0.25, relheight=0.2)

equal_btn = ttk.Button(btn_frame, text='+/-', style='my.TButton',
                       command=minus_sign_func)
equal_btn.place(relx=0.0, rely=0.8,
                relwidth=0.25, relheight=0.2)

equal_btn = ttk.Button(btn_frame, text='=', style='my.TButton',
                       command=lambda: action('='))
equal_btn.place(relx=0.75, rely=0.8,
                relwidth=0.25, relheight=0.2)

"""
max = 28
for y in range(0, 5):
    for x in range(1, 8):
        if (x+y*7) <= max:
            print(x+y*7, ',', end='')
    print()
"""

root.mainloop()
