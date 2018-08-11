import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def testFunc(self):
        print("test")

    def createWidgets(self):
        self.consumerKeyEntry = tk.Entry()
        self.consumerKeyEntry.pack()

        self.consumerSecretEntry = tk.Entry()
        self.consumerSecretEntry.pack()

        self.accessKeyEntry = tk.Entry()
        self.accessKeyEntry.pack()

        self.accessSecretEntry = tk.Entry()
        self.accessSecretEntry.pack()

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)

        self.QUIT.pack(side="bottom")

        self.update = tk.Button(self, text="Update Settings", command=self.testFunc)
        self.update.pack()


root = tk.Tk()
root.geometry("300x300")
root.title("Settings")
root.resizable(False, False)

app = Application(master=root)
app.mainloop()
