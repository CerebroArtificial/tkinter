# <center>Creating a graphical user interface in Python - Tkinter Part 1</center>

https://steemitimages.com/0x0/https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2000px-Python_logo_and_wordmark.svg.png

#### Repository 
https://github.com/python/cpython

#### What Will I Learn?
- Import from Tkinter
- Create a basic window
- Understand Marcos
- Create a top and bottom frame
- Design of a window
- Geometry Manager Pack

#### Requirements
You must have knowledge about the Python syntax.

- A PC/laptop with any Operating system such as Linux, Mac OSX, Windows OS.

Note: This tutorial is performed in Sublime Text 3 in laptop with Windows 7, 32 bit OS, Python 3.6.4.

#### Difficulty
- Intermediate

## <center>Creating a graphical user interface in Python - Tkinter Part 1</center>

Welcome to the first part of the tutorial on how to create graphical interfaces with Tkinter in Python. The main objective of this tutorial is to introduce the developer who is not familiar with the programming of GUI in Tkinter. For this, we will follow a series of examples that show, in a progressive way, the use of the necessary elements to build a graphic application: windows, geometry managers, widgets, menus, event management, sources, styles and themes.

#### <center>Let's start!</center>

#### Tkinter

Tkinter is a Python programming language library oriented to the graphical interface for desktop applications. Tkinter comes installed by default in Python, so it is not necessary to install it.

#### Create a basic window

A window is the fundamental element of a GUI application. It is the first object that is created and on this the rest of the widgets objects (labels, buttons, etc.)

To import the library we use <code>from tkinter import *</code>

~~~
from tkinter import * #import the library

root = Tk () #Create the main window

root.mainloop () # Prevents the program from closing
~~~
<br>

<center>https://s19.postimg.cc/vdxc3q237/Screenshot_17.jpg</center>

* With <code> root = Tk () </code> we assign to the variable <code> root </code> the most basic Tkinter <code> Tk () </code> function that generates a window.

* <code> root.mainLoop () </code> is the main loop and performs the function of constantly keeping the window on our desktop.

#### Modifying the window

In addition to Tk (), we can declare more variables to modify our window, such as:

* <code>config(bg=" ") </code>: Coloring the interior of the window
* <code>geometry("NxN") </code>: Change the size of the window.
* <code>title(" ")</code>: Assign a title to the window.
* <code>Button( )</code>:  Place a button in the window
* <code>Label( ) </code>: Place a text
* <code>iconbitmap('.ico')</code>:  Place icon to the window
* <code>Toplevel( )</code>: Create a new window
* <code>Frame ( ) </code>: Place the panels to sort the elements
* <code>Canvas ( ) </code>: To draw and graph functions etc
* <code>Entry ( )</code>: Place a text entry of a line
* <code>Text ( )</code>: Place a text entry of several lines
* <code> Listbox ( )</code>: Place a list with clickable elements
* <code>Menu ( )</code>: Places a menu that can contain waterfalls and clickable elements
* <code> Message ( )</code>: Place a text

For example:
~~~
from tkinter import * #We import the library

root = Tk() #We create the main window

root.title('Application') #Assign a title to the window
root.config(bg="black") #Coloring the interior of the window
root.geometry('300x300') #Change the size of the window
root.iconbitmap('favicon.ico')

root.mainloop() #Prevent the program from closing
~~~

<center>https://s19.postimg.cc/q6c8ywb3n/Screenshot_19.jpg</center>

#### Designing graphic windows  for a mini application

To define how widgets should be placed inside a window, geometry managers are used. Tkinter has three geometry managers: package, grid and place. If an application has several windows, each of them can be built with any of these managers, indistinctly.

To build windows, special widgets are used, such as frames, panels, etc., which act as containers for other widgets. These widgets are used to group several controls in order to facilitate the operation of the users.

---

Next, we will know the characteristics of the geometric manager Pack with an application.

The application consists of a typical window to access a system that displays the current user account of the computer in an entry box and presents another box to enter your password. In the lower part there are two buttons: one with the text 'Accept' to validate the password and another with 'Cancel' to end the application.

#### The Geometry Manager Pack

With this manager the organization of the widgets is done taking into account the sides of a window: up, down, right and left.

If several controls are located on the top side or on the left side of a window, we will build a vertical bar or a horizontal bar of controls. Although it is ideal for simple designs, it can also be used with complex designs. In addition, it is possible to make the controls adjust to the size changes of the window.

We call the libraries to use in our project
~~~
from tkinter import *
from tkinter import ttk, font
import getpass
~~~

We will work with an object called application <code> class Application (): </code>

Initialize our attributes of the objects that we created in the <code>__init__</code> method

~~~
    def __init__(self):
        self.root = Tk()
        self.root.title("Acces")
~~~
We change the format of the letter with the <code> Font </code> module that we import. <code>source=font.Font(weight='bold')</code>

We define the labels that accompany the input boxes and assign the previous font format:
~~~
        self.etiq1 = ttk.Label(self.root, text="User:", font=source)
        self.etiq2 = ttk.Label(self.root, text="Password:", font=source)
~~~

We declare two variables of type string to contain the user and the password:

~~~
        self.user1 = StringVar()
        self.key = StringVar()
~~~

We read the name of the user who initiates the session in the system and assign it to the variable <code> self.user1 </code>.

~~~
        self.user1.set(getpass.getuser())
~~~

We define two input boxes that will accept strings with a maximum length of 30 characters.

* In the first one of them <code>'self.ctext1'</code> that will contain the name of the user, the variable <code>'self.user1'</code> is assigned to the option <code>'textvariable'</code>. Any value that the variable takes during program execution will be reflected in the input box.
* In the second entry box, it will be the password, the same is done. In addition, the option <code>'show'</code> is established with an <code>"*"</code> to hide the writing of the passwords:

~~~
        self.ctext1 = ttk.Entry(self.root, textvariable=self.user1, width=30)
        self.ctext2 = ttk.Entry(self.root, textvariable=self.key, width=30, show="*")
        self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL)
~~~

Two buttons are defined with two methods: The <code>'Accept'</code> button will call the <code>'self.accept'</code> method when pressed to validate the password; and the <code>'Cancel'</code> button will terminate the application if it happens to press:

~~~
        self.button1 = ttk.Button(self.root, text="Accept", command=self.acept1)
        self.button2 = ttk.Button(self.root, text="Cancel", command=quit)                         
~~~

The positions of the widgets within the window are defined. All controls are placed on the upper side, except for the last two buttons, which will be placed below the last <code>"TOP"</code>: the first button on the left side and the second on the right.

~~~
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.button1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.button2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
~~~

The <code>'padx'</code> and <code>'pady'</code> options are used to add extra horizontal and / or vertical external space to the widgets to separate them from each other and from the edges of the window. There are other equivalents that add extra internal space: <code>'ipadx'</code> and <code>'ipady'</code>.

We place so that when starting the program the focus is assigned to the password entry box so that you can start writing directly:

~~~
        self.ctext2.focus_set()
        self.root.mainloop()
~~~

The <code>'accept1'</code> method will be used to validate the entered password. It will be called when the <code>'OK'</code> button is pressed. If the password matches the string <code>'utopian'</code> the message <code>'Access allowed'</code> and the accepted values will be printed. Otherwise, the message <code>'Access Denied'</code> will be displayed and the focus will return to the same place.

~~~
    def acept1(self):
        if self.key.get() == 'utopian':
            print("Access allowed")
            print("User:   ", self.ctext1.get())
            print("Password:", self.ctext2.get())
        else:
            print("Access denied")
~~~

Finally the variable <code>'self.key'</code> is initialized so that the widget <code>'self.ctext2'</code> is clean, the focus is reassigned to this widget in order to write a new password.

~~~
            self.key.set("")
            self.ctext2.focus_set()

def main():
    mi_app = Application()
    return 0

if __name__ == '__main__':
    main()
~~~

<center>https://s19.postimg.cc/gkrvaclxf/Screenshot_21.jpg</center>

## What did we learn?

This first episode was thought of as an introduction to the Python Tkinter library, which allows to create graphic interfaces in a simple way. We saw the basic syntax of Tkinter and created a mini-project of user authentication.

For the second part we will work with another Tkinter project, where we will elaborate the graphic interface of a calculator.

<center>Thanks for your time!</center>
