import tkinter as tk
from gtts import gTTS
import playsound
from pygame import mixer
from tkinter import Label,Button,Entry,StringVar,Toplevel,Text

class Window:
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.label = Label(root,text='Text_to_Speech', font='arial 20 bold', bg='white smoke',fg='blue').pack()
        self.label2 = Label(root,text='Data Flair', font='arial 15 bold', bg='white smoke',fg='blue').pack(side=tk.BOTTOM)

        self.label3 = Label(root,text='Enter Text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

        self.Msg = StringVar()
        self.E1 = Entry(root,textvariable = self.Msg, width='50')
        self.E1.place(x=20, y=100)
        
        self.btn = Button(root,text="Play",fg='green',font="arial 15 bold", command=self.Text_to_speech,width=4)
        self.btn.place(x=25, y=140)
        self.btn2 = Button(root,text="Exit",font="arial 15 bold", command=self.Exit,bg='OrangeRed1')
        self.btn2.place(x=100, y=140)
        self.btn3 = Button(root,text="Reset",font="arial 15 bold", command=self.Reset)
        self.btn3.place(x=175, y=140)
        self.btn4 = Button(root,text="Text",font="arial 15 bold", command=self.Write_text)
        self.btn4.place(x=25, y=200)

       
    def Text_to_speech(self):
        self.Message = self.E1.get()
        self.speech = gTTS(text = self.Message ,lang="tr")
        self.speech.save('DataFlair.mp3')
        mixer.init()
        mixer.music.load('./DataFlair.mp3')  #add path
        mixer.music.play()
        
    def Exit(self):
        self.root.destroy()

    def Reset(self):
        self.Msg.set("")

    def Write_text(self):
        self.newWindow = Toplevel(self.root)
        self.pencere = Other_Window(self.newWindow)


class Other_Window(Window):
    def __init__(self,newWindow):
        
        self.newWindow = newWindow
        self.newWindow.geometry('550x500')
        self.newWindow.resizable(0,0)
        self.newWindow.config(bg='ghost white')
        self.newWindow.title('Text_to_Speech')
        
        self.label = Label(newWindow,text='Text_to_Speech', font='arial 20 bold', bg='white smoke',fg='blue').pack()
        self.label2 = Label(newWindow,text='Please Entry File Name Above', font='arial 15 bold', bg='white smoke').pack(side=tk.BOTTOM)

        self.label3 = Label(newWindow,text='Enter Text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

        self.prag = Text(newWindow,fg = "blue",font="Helvetica 13 bold",height=15,width = 52)
        self.prag.place(x=20,y=100)

        self.path = StringVar()
        self.E2 = Entry(newWindow,textvariable = self.path, width='50')
        self.E2.pack(side=tk.BOTTOM)

        self.btn = Button(newWindow,text="Play",fg='green',font="arial 15 bold", command=self.Text_to_speech,width=4)
        self.btn.place(x=25, y=400)
        self.btn3 = Button(newWindow,text="Reset",font="arial 15 bold", command=self.Reset)
        self.btn3.place(x=100, y=400)

    def Reset(self):
        self.prag.delete("1.0","end")

    def Text_to_speech(self):
        self.Message = self.prag.get("1.0","end")
        self.speech = gTTS(text = self.Message ,lang="tr")
        self.file_name = self.E2.get()
        self.speech.save(self.file_name+'.mp3')
        mixer.init()
        mixer.music.load('./'+self.file_name+'.mp3')  #add path
        mixer.music.play()
        
        
pen = tk.Tk()
pen.geometry('350x300')
pen.resizable(0,0)
pen.config(bg='ghost white')
pen.title('DataFlair - Text_to_Speech')
pencere = Window(pen)
pen.mainloop()
            
