# import relevant libraries

import tkinter as tk
from tkinter import messagebox
from tkhtmlview import HTMLLabel
import webbrowser


def info():
    """
    Creates the Information and help page of Application.

    Parameters:
        info_tab: The information and help window root object.
        info_label(HTMLLabel): Label for information and help description on this window.

    Returns:
        None.
    """
    info_tab = tk.Toplevel()  # create the info_tab window on top of MainWindow
    info_tab.title("Information and help page")  # gives title to the info_tab window
    info_tab.iconbitmap("win_icon.ico")  # assigns icon image to the info_tab window
    info_tab.geometry("800x550")  # defines geometry of the info_tab window

    info_label = HTMLLabel(info_tab, html='\
                <code><h2 style="color: brown; font-family:Georgia;\
                text-align: center">Information and Help</h2></code>\
                <p>@HUMANIA(NGO based in Cologne Germany)\
                we are helping refugees who are coming to this region.\
                Currently, we are able to provide the following facilities:</p>\
                <ul>\
                <li>Clothing and fooding</li>\
                <li>Lodging</li> \
                <li>Social Services</li>\
                <li>Others</li>\
                </ul>\
                ')
    info_label.pack(pady=40, padx=20, fill="both", expand=True)

    # exit button to close info_tab window
    tk.Button(info_tab, text="Exit", width=8, bg="brown", fg="white", font="Georgia 12",
              command=info_tab.destroy).place(x=370, y=450)
    info_tab.mainloop()  # start the program via main event loop


def about():
    """
    Creates the about page of Application.

    Parameters:
        abt_tab: The about us window root object.
        label_about(HTMLLabel): Label describing about us window.

    Returns:
        None.
    """
    abt_tab = tk.Toplevel()  # create the abt_tab window on top of MainWindow
    abt_tab.title("About us")  # gives title to the abt_tab window
    abt_tab.iconbitmap("win_icon.ico")  # assigns icon image to the info_tab window
    abt_tab.geometry("800x550")  # defines geometry of the info_tab window
    label_about = HTMLLabel(abt_tab, html='\
                        <code><h3 style="color: brown; font-family:Georgia">About us</h3></code>\
                        <p>We are a small group of dedicated individuals wanting to make\
                        a change in society by helping people in need.\
                        The world is experiencing a surge in refugees which is painful\
                        to see and experience. We understand the pain and sufferings and\
                        that is why @Humania we try our best to help those people fleeing\
                        war torn areas to get shelter, food , medicine and all basic help\
                        which may make a difference in their life. We totally believe that \
                        A friend in need is a friend indeed. Our Organisation is self\
                        funded and we are getting generous donations as well from people  who care.\
                        With the help of people we have brought changes in the lives of \
                        over hundreds of families till now.</p>\
                    ')
    label_about.pack(padx=20, pady=40, fill="both", expand=True)

    # exit button to close abt_tab window
    tk.Button(abt_tab, text="Exit", width=8, bg="brown", fg="white", font="Georgia 12",
              command=abt_tab.destroy).place(x=360, y=450)

    abt_tab.mainloop()


def contact():
    """
    Creates the Contact page of Application.

    Parameters:
        contact_tab: The contact window root object.
        label_contact(HTMLLabel): Label  contact window.

    Returns:
        None.
    """
    contact_tab = tk.Toplevel()  # create the contact_tab window on top of MainWindow
    contact_tab.title("Contact Us")  # gives title to the contact_tab window
    contact_tab.iconbitmap("win_icon.ico")  # assigns icon image to the contact_tab window
    contact_tab.geometry("500x450")  # defines geometry of the contact_tab window

    label_frame = tk.LabelFrame(contact_tab, text="Contact Us")
    label_frame.pack(fill="both", pady=30, padx=30)

    label_contact = tk.Label(label_frame, text="Abc-def Straße 15\n50226 Frechen\nFrechen@abc.de\n\
                                         \n+49 12346789\n*These calls are free for you\n\nMo: 08:00 AM - 12:00 PM")
    label_contact.pack(padx=10, pady=10)

    # exit button to close contact_tab window
    tk.Button(contact_tab, text="Exit", width=8, bg="brown", fg="white", font="Georgia 10",
              command=contact_tab.destroy).place(x=230, y=350)


def clothing_food_services():
    """
    Opens Webpage of food services on local host machine.

    Args: None.

    Returns: None.
    """
    webbrowser.open("Food.html")


def social_security():
    """
    Opens Arbeit's Agentur Webpage.

    Args: None.

    Returns: None.
    """
    webbrowser.open("https://www.arbeitsagentur.de")


def oth_services():
    """
    A display of messagebox with an error message.

    Args: None.

    Returns: None.
    """
    messagebox.showerror("Other Services", "Sorry, not available at the moment !")

