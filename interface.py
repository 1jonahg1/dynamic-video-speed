from tkinter import *
import tkinter.font as tkFont

class MyWindow:
    def __init__(self, window):
        window.iconbitmap('flash.ico')
        self.title=Label(window, text="Change Lecture Speed to the Ideal Speed For You", fg='black', font=("Helvetica", 14))
        self.title.pack()
        self.f = tkFont.Font(self.title, self.title.cget("font"))
        self.f.configure(underline = True)
        self.title.configure(font=self.f)
        self.title.place(x=75, y=45)

        self.test=Button(window, text="Test Speed", fg='white',bg='grey',command=self.Test)
        self.test.place(x=260, y=270)

        self.finish=Button(window, text="Speed Up!", fg='white',bg='green',command=self.Finish)
        self.finish.place(x=260, y=310)
        
        self.wpm_txt=Label(window, text="Enter Words Per Minute", fg='black', font=("Helvetica", 10))
        self.wpm_txt.place(x=122, y=120)
        self.wpm=Entry(window, bg='white',fg='black', bd=5)
        self.wpm.place(x=130, y=150)
        
        self.languages=Listbox(window, height=5, selectmode='single')
        self.languages.insert(END,"English")
        self.languages.insert(END,"Hebrew")
        self.languages.insert(END,"French")
        self.languages.place(x=320, y=150)
        self.languages.select_set(0) #first Language set as default 
        self.language_txt=Label(window, text="Video Language", fg='black', font=("Helvetica", 10))
        self.language_txt.place(x=328, y=120)
        
    def Finish (self):
        input_language = self.languages.get(self.languages.curselection()[0]) 
        input_wpm = int(self.wpm.get())
        print("Input Language: " + str(input_language) + "\n" + "Input WPM: " + str(input_wpm))
 
    def Test (self):
        input_wpm = int(self.wpm.get())
        print("Input WPM: " + str(input_wpm))
        #add 10 sec audio to test
    

window=Tk()
window.title('Video Speed Manager')
window.geometry("600x400+10+20")
mywin=MyWindow(window)
window.mainloop()






