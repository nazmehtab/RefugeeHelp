# import relevant libraries

import tkinter as tk
import sqlite3
from tkinter import messagebox


class Database(object):
    """
        Class to create sqlite database `details_book` and query table `detail` from the database
        and create db_window to perform queries onto the database.

        Methods:
            update(): Updates the record of the user in `detail` table with given rowid.
            delete(): Deletes the record of the user in `detail` table with given rowid.
            submit(): Add record of the new user in `detail` table.
            show(): Displays the record of the user with given rowid, in the entry boxes.
            __del__(): Destructor method to close the database connection.
    """

    def __init__(self):
        """Constructs all the necessary parameters for the Database object."""
        self.db_window = tk.Toplevel()  # create the db_window on top of MainWindow
        self.db_window.title("Housing Services")  # gives title to the db_window
        self.db_window.iconbitmap("win_icon.ico")  # assigns icon image to the db_window
        self.db_window.geometry("480x530")  # defines geometry of the db_window

        # establish a connection with sqlite database details_book or create one if it doesn't exist
        self.conn = sqlite3.connect('details_book.db')
        self.c = self.conn.cursor()  # create a cursor

        # create the `detail` table into the database
        self.c.execute("""CREATE TABLE IF NOT EXISTS detail(
             first_name text,
             last_name text,
             contact integer,
             email text,
             origin text,
             members integer
             )""")

        # creating label to fill the form
        self.info_label = tk.Label(self.db_window,
                                   text="Please fill out the form below and We'll get back to you as soon as possible.")
        self.info_label.grid(row=1, columnspan=3, padx=20, pady=20)

        # creating text boxes labels
        self.f_name_label = tk.Label(self.db_window, text='First Name*')
        self.f_name_label.grid(row=2, column=1, pady=(5, 0))
        self.l_name_label = tk.Label(self.db_window, text='Last Name*')
        self.l_name_label.grid(row=3, column=1, pady=5)
        self.contact_label = tk.Label(self.db_window, text='Contact*')
        self.contact_label.grid(row=4, column=1, pady=5)
        self.email_label = tk.Label(self.db_window, text='E-Mail')
        self.email_label.grid(row=5, column=1, pady=5)
        self.origin_label = tk.Label(self.db_window, text='Origin Country')
        self.origin_label.grid(row=6, column=1, pady=5)
        self.members_label = tk.Label(self.db_window, text='Family Members')
        self.members_label.grid(row=7, column=1, pady=5)

        # creating text boxes
        self.f_name = tk.Entry(self.db_window, width=30)
        self.f_name.grid(row=2, column=2, padx=20)
        self.l_name = tk.Entry(self.db_window, width=30)
        self.l_name.grid(row=3, column=2, padx=20)
        self.contact = tk.Entry(self.db_window, width=30)
        self.contact.grid(row=4, column=2, padx=20)
        self.email = tk.Entry(self.db_window, width=30)
        self.email.grid(row=5, column=2, padx=20)
        self.origin = tk.Entry(self.db_window, width=30)
        self.origin.grid(row=6, column=2, padx=20)
        self.members = tk.Entry(self.db_window, width=30)
        self.members.grid(row=7, column=2, padx=20)

        # submit button to add new record to the database detail_book.db
        self.submit_btn = tk.Button(self.db_window, text='Add Record to Database', command=self.submit)
        self.submit_btn.grid(row=8, column=1, columnspan=2, padx=10, pady=10, ipadx=111)

        # label for other possibilities
        self.info_label = tk.Label(self.db_window, text="Other possibilities: ")
        self.info_label.grid(row=10, columnspan=3, padx=20, pady=20)

        # text box label for select id
        self.id_box_label = tk.Label(self.db_window, text="Select ID")
        self.id_box_label.grid(row=12, column=1)

        # text box to select user id
        self.id_box = tk.Entry(self.db_window, width=30)
        self.id_box.grid(row=12, column=2, pady=5)

        # button to display user record
        self.show_btn = tk.Button(self.db_window, text='Show Record', command=self.show)
        self.show_btn.grid(row=13, column=1, columnspan=2, padx=10, pady=10, ipadx=137)

        # button to delete user record
        self.delete_btn = tk.Button(self.db_window, text='Delete Records', command=self.delete)
        self.delete_btn.grid(row=14, column=1, columnspan=2, padx=10, pady=10, ipadx=136)

        # button to update user record
        self.edit_btn = tk.Button(self.db_window, text='Edit Record', command=self.update)
        self.edit_btn.grid(row=15, column=1, columnspan=2, padx=10, pady=10, ipadx=146)

        self.conn.commit()  # save(commit) the changes
        self.db_window.mainloop()  # start the program via main event loop

    def update(self):
        """
        The function updates the record of the user in `detail` table with given rowid.

        Parameters:
            first_name(text): First name of the user.
            last_name(text): Last name of the user.
            contact(integer): Contact number of the user.
            email(text): E-mail address of the user.
            origin(text): Country of origin of the user.
            members(integer): Total family members of the user.
            oid(integer): SQLite implicitly creates a column named rowid
            ``can be referred with aliases: _rowid_ and oid`` in detail table.

        Raises:
            Exception: When record with given rowid does not exist in detail table.
        """
        try:
            # update the record in the detail table, whose rowid is given in the id entry box
            self.c.execute("""UPDATE detail SET
                    first_name = :f_name,
                    last_name = :l_name, 
                    contact = :contact,
                    email = :email,
                    origin = :origin,
                    members = :members
    
                    WHERE oid = :oid""",
                           {
                               'f_name': self.f_name.get(),
                               'l_name': self.l_name.get(),
                               'contact': self.contact.get(),
                               'email': self.email.get(),
                               'origin': self.origin.get(),
                               'members': self.members.get(),
                               'oid': self.id_box.get(),
                           })

            # emptying the text boxes after the record is updated
            self.id_box.delete(0, tk.END)
            self.f_name.delete(0, tk.END)
            self.l_name.delete(0, tk.END)
            self.contact.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.origin.delete(0, tk.END)
            self.members.delete(0, tk.END)

            messagebox.showinfo("Updated", "Record updated successfully !")
            self.conn.commit()
        except:  # When record with given rowid does not exist in detail table.
            pass  # pass the error

    def delete(self):
        """
           The function deletes the record of the user in `detail` table with given rowid.

           Parameters:
               oid(integer): SQLite implicitly creates a column named rowid
               ``can be referred with aliases: _rowid_ and oid`` in detail table.

           Raises:
               Exception: When record with given rowid does not exist in detail table.
        """
        try:
            # delete the record from the detail table, whose rowid is given in the id entry box
            self.c.execute("DELETE from detail WHERE oid= " + self.id_box.get())
            self.id_box.delete(0, tk.END)  # empty id box after the record is deleted
            self.conn.commit()  # save(commit) the changes
            messagebox.showinfo("Deleted", "Record deleted successfully !")  # messagebox to show given message
        except:  # When record with given rowid does not exist in detail table.
            pass  # pass the eroor

    def submit(self):
        """
           The function add record of the new user in `detail` table.

           Parameters:
               f_name(text): First name of the user.
               l_name(text): Last name of the user.
               contact(integer): Contact number of the user.
               email(text): E-mail address of the user.
               origin(text): Country of origin of the user.
               members(integer): Total family members of the user.
               oid(integer): SQLite implicitly creates a column named rowid
               ``can be referred with aliases: _rowid_ and oid`` in detail table.
        """
        # insert a new record in to the table with values given in the entry boxes
        self.c.execute("INSERT INTO detail VALUES(:f_name, :l_name, :contact, :email, :origin, :members)",
                       {
                           'f_name': self.f_name.get(),
                           'l_name': self.l_name.get(),
                           'contact': self.contact.get(),
                           'email': self.email.get(),
                           'origin': self.origin.get(),
                           'members': self.members.get()
                       })

        # emptying the boxes after the record is inserted
        self.f_name.delete(0, tk.END)
        self.l_name.delete(0, tk.END)
        self.contact.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.origin.delete(0, tk.END)
        self.members.delete(0, tk.END)

        # messagebox to show given message
        messagebox.showinfo("Details saved", "We'll get back to you as soon as possible !")

        self.conn.commit()  # save(commit) the changes

    def show(self):
        """
           The function displays the record of the user with given rowid, in the entry boxes.

           Parameters:
               f_name(text): First name of the user.
               l_name(text): Last name of the user.
               contact(integer): Contact number of the user.
               email(text): E-mail address of the user.
               origin(text): Country of origin of the user.
               members(integer): Total family members of the user.
               oid(integer): SQLite implicitly creates a column named rowid
               ``can be referred with aliases: _rowid_ and oid`` in detail table.

           Raises:
               Exception: When record with given rowid does not exist in the detail table.
        """
        try:
            # grab a user record from the detail table, whose rowid is given in the id entry box
            self.c.execute('SELECT * FROM detail WHERE oid =' + self.id_box.get())
            # fetch all the records from detail table
            records = self.c.fetchall()
            for record in records:
                # displaying the record in text box labels
                self.f_name.insert(tk.END, record[0])
                self.l_name.insert(tk.END, record[1])
                self.contact.insert(tk.END, record[2])
                self.email.insert(tk.END, record[3])
                self.origin.insert(tk.END, record[4])
                self.members.insert(tk.END, record[5])

            self.id_box.delete(0, tk.END)  # empty to delete box after record has been displayed
            self.conn.commit()  # save(commit) the changes
        except:  # When record with given rowid does not exist in detail table.
            pass  # pass the error

    def __del__(self):
        """ Destructor method __del__ to close the database connection"""
        self.conn.close()  # closes connection with sqlite database details_book
