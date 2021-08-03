from tkinter import *
window = Tk()
window.geometry('500x354')
window.resizable(0, 0)
window.title('Calculator')


def click(item):
    global expression
    expression += str(item)
    input_text.set(expression)


def clear():
    global expression
    expression = ""
    input_text.set("")


def egalitate():
    try:
        global expression
        rezultat = str(eval(expression))
        input_text.set(rezultat)
        expression = ""
    except Exception:
        expression = ""
        input_text.set("Error! Please click C button")


expression = ''
input_text = StringVar()

input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground='black', highlightcolor='black',
                    highlightthickness=1)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg='#eee', bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

frame_butoane = Frame(window, width=500, height=304, bg='grey')
frame_butoane.pack()

buton_clear = Button(frame_butoane, text='C', fg='black', width=38, height=3, bd=0, bg='#eee', cursor='hand2',
                     command=lambda : clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
impartit = Button(frame_butoane, text='/', fg='black', width=10, height=3, bd=0, bg='#FFA500', cursor='hand2',
                  command= lambda : click('/')).grid(row=0, column=3, padx=1, pady=1)


sapte = Button(frame_butoane, text='7', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('7')).grid(row=1, column=0, padx=1, pady=1)
opt = Button(frame_butoane, text='8', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('8')).grid(row=1, column=1, padx=1, pady=1)
noua = Button(frame_butoane, text='9', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('9')).grid(row=1, column=2, padx=1, pady=1)
inmultire = Button(frame_butoane, text='*', fg='black', width=10, height=3, bd=0, bg='#FFA500', cursor='hand2',
                  command= lambda : click('*')).grid(row=1, column=3, padx=1, pady=1)


patru = Button(frame_butoane, text='4', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('4')).grid(row=2, column=0, padx=1, pady=1)
cinci = Button(frame_butoane, text='5', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('5')).grid(row=2, column=1, padx=1, pady=1)
sase = Button(frame_butoane, text='6', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('6')).grid(row=2, column=2, padx=1, pady=1)
minus = Button(frame_butoane, text='-', fg='black', width=10, height=3, bd=0, bg='#FFA500', cursor='hand2',
                  command= lambda : click('-')).grid(row=2, column=3, padx=1, pady=1)


unu = Button(frame_butoane, text='1', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('1')).grid(row=3, column=0, padx=1, pady=1)
doi = Button(frame_butoane, text='2', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('2')).grid(row=3, column=1, padx=1, pady=1)
trei = Button(frame_butoane, text='3', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('3')).grid(row=3, column=2, padx=1, pady=1)
plus = Button(frame_butoane, text='+', fg='black', width=10, height=3, bd=0, bg='#FFA500', cursor='hand2',
                  command= lambda : click('+')).grid(row=3, column=3, padx=1, pady=1)

zero = Button(frame_butoane, text='0', fg='black', width=24, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('0')).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
virgula = Button(frame_butoane, text=',', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : click('.')).grid(row=4, column=2, padx=1, pady=1)
egal = Button(frame_butoane, text='=', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command= lambda : egalitate()).grid(row=4, column=3, padx=1, pady=1)

window.mainloop()
