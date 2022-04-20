# import relevant libraries

from tkinter import *
from PIL import ImageTk, Image
from info import *
from DB import Database


class MainWindow(object):
    """
    Main Window of the Application.

    Args:
        root: The MainWindow Tk root object.

    Attributes:
        bg_pic(PhotoImage): Image attribute of background image.
        my_canvas(Canvas): Canvas attribute for background image.
        label1-label9(Label): Display text widgets on the MainWindow.
        btn1-btn4(Button): Action buttons on the MainWindow.
        btn5-btn7(Button): Navigation buttons on the MainWindow.
        img1-img7(PhotoImage): Image attributes of 7 images.
        img_about(PhotoImage): about image icon placed before 'About us' navigation button.
        img_info(PhotoImage): information image icon placed before 'Information and help' navigation button.
        img_contact(PhotoImage): contact image icon placed before 'Contact' navigation button.
        our_images(list(PhotoImage)): list of 7 images for slideshow on MainWindow.

    Methods:
        next_image():
            The Method is running image slideshow on MainWindow.
    """

    def __init__(self, root):
        """
        MainWindow class constructor to initialize the root object.
        """
        self.bg_pic = ImageTk.PhotoImage(Image.open("images/Cologne_bridge.jpg").resize((800, 200), Image.ANTIALIAS))
        self.my_canvas = Canvas(root, width=800, height=200, highlightthickness=0)
        self.my_canvas.pack(fill='both', expand=True)
        self.my_canvas.create_image(0, 0, image=self.bg_pic, anchor="nw")
        self.my_canvas.create_text(400, 40, text="@HUMANIA", font="Georgia 20", fill="white")
        self.my_canvas.create_text(400, 65, text="A REFUGEE NGO", font="Georgia 11", fill="white")

        # create labels
        self.label1 = Label(root, font="bold", bd=0)
        self.label1.place(y=200)

        self.label2 = Label(root, text="We are happy to assist you!", font="Georgia 15", fg="brown")
        self.label2.place(x=445, y=220)

        self.label3 = Label(root, text="Please select one of our services...", font="Georgia 13", fg="brown")
        self.label3.place(x=450, y=260)

        self.label4 = Label(root, text="Help and Information", font="Georgia 15", fg="brown")
        self.label4.place(x=445, y=220)

        self.label5 = Label(root, text="Contact Us", font="Georgia 15", fg="brown")
        self.label5.place(x=445, y=220)

        self.label6 = Label(root, text="We are happy to assist you!", font="Georgia 15", fg="brown")
        self.label6.place(x=445, y=220)

        self.img_about = ImageTk.PhotoImage(Image.open("images/address.png").resize((15, 20), Image.ANTIALIAS))

        self.label7 = Label(root)
        self.label7.place(x=360, y=520)
        self.label7.config(image=self.img_about)

        self.img_info = ImageTk.PhotoImage(Image.open("images/information.png").resize((15, 20), Image.ANTIALIAS))

        self.label8 = Label(root)
        self.label8.place(x=512, y=518)
        self.label8.config(image=self.img_info)

        self.img_contact = ImageTk.PhotoImage(Image.open("images/cont.png").resize((15, 20), Image.ANTIALIAS))

        self.label9 = Label(root)
        self.label9.place(x=700, y=520)
        self.label9.config(image=self.img_contact)

        # create buttons
        self.btn1 = HoverButton1(root, text="Clothing and Food Services", font="Georgia 13", fg="white", bg="brown",
                                 command=clothing_food_services, relief="ridge", activebackground="white", width=23)
        self.btn1.place(x=452, y=300)

        self.btn2 = HoverButton1(root, text="Housing Services", font="Georgia 13", fg="white", bg="brown",
                                 command=Database, relief="ridge", activebackground="white", width=23)
        self.btn2.place(x=452, y=350)

        self.btn3 = HoverButton1(root, text="Social Security", font="Georgia 13", fg="white", bg="brown",
                                 relief="ridge", command=social_security, activebackground="white", width=23)
        self.btn3.place(x=452, y=400)

        self.btn4 = HoverButton1(root, text="Other Services", font="Georgia 13", fg="white", bg="brown",
                                 relief="ridge", command=oth_services, activebackground="white", width=23)
        self.btn4.place(x=452, y=450)

        self.btn5 = HoverButton2(root, text='About us', relief='flat', command=about, fg="gray")
        self.btn5.place(x=380, y=520)

        self.btn6 = HoverButton2(root, text='Information and help', relief='flat', command=info, fg="gray")
        self.btn6.place(x=531, y=520)

        self.btn7 = HoverButton2(root, text='Contact', relief='flat', command=contact, fg="gray")
        self.btn7.place(x=720, y=520)

        # open images to use with label1 on the MainWindow
        img1 = ImageTk.PhotoImage(Image.open("images/image1.jpg").resize((340, 400), Image.ANTIALIAS))
        img2 = ImageTk.PhotoImage(Image.open("images/image2.jpg").resize((340, 400), Image.ANTIALIAS))
        img3 = ImageTk.PhotoImage(Image.open("images/image3.jpg").resize((340, 400), Image.ANTIALIAS))
        img4 = ImageTk.PhotoImage(Image.open("images/image4.jpg").resize((340, 400), Image.ANTIALIAS))
        img5 = ImageTk.PhotoImage(Image.open("images/image5.png").resize((340, 400), Image.ANTIALIAS))
        img6 = ImageTk.PhotoImage(Image.open("images/image6.jpg").resize((340, 400), Image.ANTIALIAS))
        img7 = ImageTk.PhotoImage(Image.open("images/image6.jpg").resize((340, 400), Image.ANTIALIAS))

        our_images = [img1, img2, img3, img4, img5, img6, img7]  # create list of 7 images

        def next_image():
            """
            The Method is running image slideshow on the MainWindow.

            Parameters:
                img_count(int): an iterator for image count.
                label1(Label): a label widget to configure image slideshow on MainWindow.
            """
            global img_count
            if img_count == 7:
                self.label1.config(image=our_images[0])  # configure the image to the label1
                img_count = 0
            else:
                self.label1.config(image=our_images[img_count])
                img_count += 1
            root.after(2500, next_image)  # tkinter built-in method `after` calling next_image method every 2.5 sec

        next_image()  # initiating call to image rotation on MainWindow


class HoverButton1(Button):
    """
    HoverButton1 inheriting the Button class that modifies the behaviour
    of the default action buttons on MainWindow when you hover.

    Args:
        root: The MainWindow Tk root object.
        **kw: Arbitrary keyword argument.
        
    Mehtods:
        on_enter(e): uses event data for the button hover event to change the background of the button.
        on_leave(e): uses the event data for the button leave event to change the background of the button.
    """

    def __init__(self, root, **kw):
        Button.__init__(self, master=root, **kw)
        self.bind("<Enter>", self.on_enter)  # Bind the enter event to the button
        self.bind("<Leave>", self.on_leave)  # Bind the leave event to the button

    def on_enter(self, e):
        """
        Function that uses the event data for the button hover event
        to change the background of the button.

        Args:
            e: Event argument.

        Returns:
            None.
        """
        self['background'] = '#d6665e'

    def on_leave(self, e):
        """
        Function that uses the event data for the button leave event
        to change the background of the button.

        Args:
            e: Event argument.

        Returns:
            None.
        """
        self['background'] = 'brown'


class HoverButton2(Button):
    """
    HoverButton2 inheriting the Button class that modifies the behaviour
    of the default navigation buttons on MainWindow when you hover.

    Args:
        root: The MainWindow Tk root object.
        **kw: Arbitrary keyword argument.
        
    Mehtods:
        on_enter(e): uses event data for the button hover event to change the foreground of the button.
        on_leave(e): uses the event data for the button leave event to change the foreground of the button.
    """

    def __init__(self, root, **kw):
        Button.__init__(self, master=root, **kw)
        self.bind("<Enter>", self.on_enter)  # Bind the enter event to the button
        self.bind("<Leave>", self.on_leave)  # Bind the leave event to the button

    def on_enter(self, e):
        """
        Function that uses the event data for the button hover event
        to change the foreground of the button.

        Args:
            e: Event argument.

        Returns:
            None.
        """
        self['foreground'] = 'brown'

    def on_leave(self, e):
        """
        Function that uses the event data for the button leave event
        to change the foreground of the button.

        Args:
            e: Event argument.

        Returns:
            None.
        """
        self['foreground'] = 'gray'


img_count = 0  # global image count variable initialized to 0

if __name__ == "__main__":
    master = Tk()  # create the application's MainWindow
    # configure the root window
    master.title("@HUMANIA")  # gives title to the MainWindow
    master.iconbitmap("win_icon.ico")  # assigns icon image to the MainWindow
    master.geometry("800x550")  # defines the geometry of the MainWindow
    app = MainWindow(master)  # call to the MainWindow manager class
    master.mainloop()  # start the program via main event loop
