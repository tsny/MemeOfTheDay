import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def Update(self):
        print("Update TODO")

    def createWidgets(self):
        self.consumerKeyLabel = tk.Label(text="Consumer Key")
        self.consumerKeyLabel.pack()
        self.consumerKeyEntry = tk.Entry(width=200)
        self.consumerKeyEntry.pack()

        self.consumerSecretLabel = tk.Label(text="Consumer Secret")
        self.consumerSecretLabel.pack()
        self.consumerSecretEntry = tk.Entry(width=200)
        self.consumerSecretEntry.pack()

        self.accessKeyLabel = tk.Label(text="Access Key")
        self.accessKeyLabel.pack()
        self.accessKeyEntry = tk.Entry(width=200)
        self.accessKeyEntry.pack()

        self.accessSecretLabel = tk.Label(text="Access Secret")
        self.accessSecretLabel.pack()
        self.accessSecretEntry = tk.Entry(width=200)
        self.accessSecretEntry.pack()

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

        self.update = tk.Button(self, text="Update Settings", command=self.Update)
        self.update.pack()


root = tk.Tk()
root.geometry("600x300")
root.title("Settings")
root.resizable(False, False)

app = Application(master=root)
app.mainloop()
