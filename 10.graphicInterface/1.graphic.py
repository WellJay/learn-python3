'''
    Python支持多种图形界面的第三方库，包括：

    Tk

    wxWidgets

    Qt

    GTK

    等等。

    但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。本章简单介绍如何使用Tkinter进行GUI编程。

    Tkinter

    我们来梳理一下概念：

    我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；

    Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；

    Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。

    所以，我们的代码只需要调用Tkinter提供的接口就可以了。

    第一个GUI程序

    使用Tkinter十分简单，我们来编写一个GUI版本的“Hello, world!”。
'''
import tkinter.messagebox as messagebox
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

'''
    小结

    Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。
'''
