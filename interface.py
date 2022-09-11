from tkinter import *
import tkinter.font as tkFont

def B1FUNCTION (position):
    inputLanguage = str(languages.get())
    inputWpm = int(wpm.get())
    print("Input Language" + inputLanguage + "\n" + "Input WPM" + str(inputWpm))

window=Tk()

title=Label(window, text="Change lecture Speed To The Ideal Speed For You", fg='black', font=("Helvetica", 14))

title.pack()
f = tkFont.Font(title, title.cget("font"))
f.configure(underline = True)
title.configure(font=f)
title.place(x=75, y=45)

finish=Button(window, text="Speed Up!", fg='white',bg='green')
finish.place(x=260, y=300)
finish.bind('<Button-1>', B1FUNCTION)

wpmTxt=Label(window, text="Enter Words Per Minute", fg='black', font=("Helvetica", 10))
wpmTxt.place(x=122, y=120)
wpm=Entry(window, bg='white',fg='black', bd=5)
wpm.place(x=130, y=150)
languages=Listbox(window, height=5, selectmode='single')
languages.insert(END,"English")
languages.insert(END,"Hebrew")
languages.insert(END,"French")
languages.place(x=320, y=150)

languageTxt=Label(window, text="Video Language", fg='black', font=("Helvetica", 10))
languageTxt.place(x=328, y=120)

window.title('Video Speed Manager')
window.geometry("600x400+10+20")
window.mainloop()



