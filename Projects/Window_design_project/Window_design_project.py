from tkinter import *
from tkinter import ttk, font
import getpass

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title("Acces")
        self.root.iconbitmap('favicon.ico')
        
        source = font.Font(weight='bold')

        self.etiq1 = ttk.Label(self.root, text="User:", font=source)
        self.etiq2 = ttk.Label(self.root, text="Password:", font=source)
        
        self.user1 = StringVar()
        self.key = StringVar()
        
        self.user1.set(getpass.getuser())
        
        self.ctext1 = ttk.Entry(self.root, textvariable=self.user1, width=30)
        self.ctext2 = ttk.Entry(self.root, textvariable=self.key, width=30, show="*")
        self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL)

        self.button1 = ttk.Button(self.root, text="Accept", command=self.acept1)
        self.button2 = ttk.Button(self.root, text="Cancel", command=quit)
                                                                        
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.button1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.button2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
        
        self.ctext2.focus_set()
        self.root.mainloop()

    def acept1(self):
        if self.key.get() == 'utopian':
            print("Access allowed")
            print("User:   ", self.ctext1.get())
            print("Password:", self.ctext2.get())
        else:
            print("Access denied")
            
            self.key.set("")
            self.ctext2.focus_set()

def main():
    mi_app = Application()
    return 0

if __name__ == '__main__':
    main()