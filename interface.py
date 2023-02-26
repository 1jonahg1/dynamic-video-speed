from tkinter import Label, Button, Listbox, END, Entry, Tk
import tkinter.font as tkFont
from tkinter import filedialog as fd
import DynamicVideoEdit


class MyWindow:
    def __init__(self, window):
        self.file_path = ''
        self.picked_file = False
        self.title = Label(window, text="Change Lecture Speed to the Ideal Speed For You", fg='black', font=("Helvetica", 14))
        self.title.pack()
        self.f = tkFont.Font(self.title, self.title.cget("font"))
        self.f.configure(underline=True)
        self.title.configure(font=self.f)
        self.title.place(x=75, y=40)
        self.file = Button(window, text="        Choose File        ", fg='white', bg='grey', command=self.select_file)
        self.file.place(x=230, y=80)
        self.test = Button(window, text="Test Speed", fg='white', bg='grey', command=self.Test)
        self.test.place(x=260, y=280)
        self.finish = Button(window, text="Speed Up!", fg='white', bg='green', command=self.Finish)
        self.finish.place(x=260, y=320)
        self.wpm_txt = Label(window, text="Enter Words Per Minute", fg='black', font=("Helvetica", 10))
        self.wpm_txt.place(x=122, y=130)
        self.wpm = Entry(window, bg='white', fg='black', bd=5)
        self.wpm.place(x=130, y=160)
        self.languages = Listbox(window, height=5, selectmode='single')
        self.languages.insert(END, "English")
        self.languages.insert(END, "Hebrew")
        self.languages.insert(END, "French")
        self.languages.place(x=320, y=160)
        self.languages.select_set(0)  # first Language set as default(English)
        self.language_txt = Label(window, text="Video Language", fg='black', font=("Helvetica", 10))
        self.language_txt.place(x=328, y=130)

    def select_file(self):
        filetypes = (('mp4 files', '*.mp4'), ('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file', initialdir='/',
                                      filetypes=filetypes)
        self.picked_file = True
        self.file_path = filename

    def Finish(self):
        input_language = self.languages.get(self.languages.curselection()[0]) 
        input_wpm = int(self.wpm.get())
        print("Input Language: " + str(input_language) + "\n" + "Input WPM: "
              + str(input_wpm))
        if not self.select_file:
            print("Select File First")
        else:
            video = DynamicVideoEdit.DynamicVideoEdit(self.file_path, input_language, input_wpm)
            clip_list = video.splitClips()
            video.update_speeds(clip_list)

    def Test(self):
        input_wpm = int(self.wpm.get())
        print("Input WPM: " + str(input_wpm))
        DynamicVideoEdit.test_update_audio()


window = Tk()
window.title('Video Speed Manager')
window.iconbitmap('flash.ico')
window.geometry("600x400+10+20")
mywin = MyWindow(window)
window.mainloop()
