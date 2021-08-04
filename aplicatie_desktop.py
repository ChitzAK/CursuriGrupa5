import tkinter

window = tkinter.Tk()
window.title("Fereastra")
bottom_frame = tkinter.Frame(window).pack(side='bottom')
top_frame = tkinter.Frame(window).pack(side='top')
label = tkinter.Label(window, text="Text label").pack()

def text_informare():
    tkinter.Label(window, text='Am apasat').pack()

button = tkinter.Button(top_frame, text='Text buton', fg='green', command=text_informare).pack(side='right')
button2 = tkinter.Button(top_frame, text='Text buton2', fg='red').pack()
button3 = tkinter.Button(bottom_frame, text='Text buton3', fg='orange').pack(side='right')
button4 = tkinter.Button(bottom_frame, text='Text buton4', fg='pink').pack(side='left')

window.mainloop()
