from tkinter import *
import tkinter.font as tkFont

def B1FUNCTION ():
    input_language = languages.get(languages.curselection()[0]) 
    input_wpm = int(wpm.get())
    print("Input Language: " + str(input_language) + "\n" + "Input WPM: " + str(input_wpm))

def B2FUNCTION ():
    input_wpm = int(wpm.get())
    print("Input WPM: " + str(input_wpm))
    #add 10 sec audio to test

window=Tk()
window.iconbitmap('flash.ico')
title=Label(window, text="Change Lecture Speed to the Ideal Speed For You", fg='black', font=("Helvetica", 14))

title.pack()
f = tkFont.Font(title, title.cget("font"))
f.configure(underline = True)
title.configure(font=f)
title.place(x=75, y=45)

test=Button(window, text="Test Speed", fg='white',bg='grey')
test.place(x=260, y=270)
test.bind('<Button-2>', B2FUNCTION)

finish=Button(window, text="Speed Up!", fg='white',bg='green')
finish.place(x=260, y=310)
finish.bind('<Button-1>', B1FUNCTION)

wpm_txt=Label(window, text="Enter Words Per Minute", fg='black', font=("Helvetica", 10))
wpm_txt.place(x=122, y=120)
wpm=Entry(window, bg='white',fg='black', bd=5)
wpm.place(x=130, y=150)
languages=Listbox(window, height=5, selectmode='single')
languages.insert(END,"English")
languages.insert(END,"Hebrew")
languages.insert(END,"French")
languages.place(x=320, y=150)
languages.select_set(0) #first item as default


language_txt=Label(window, text="Video Language", fg='black', font=("Helvetica", 10))
language_txt.place(x=328, y=120)

window.title('Video Speed Manager')
window.geometry("600x400+10+20")
window.mainloop()



