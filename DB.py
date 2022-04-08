import tkinter as tk
import sqlite3
from tkinter import messagebox


class Database(object):
    def __init__(self):
        self.db_window = tk.Toplevel()
        self.db_window.title("Housing Services")
        self.db_window.iconbitmap("win_icon.ico")
        self.db_window.geometry("480x530")

        self.conn = sqlite3.connect('details_book.db')
        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS detail(
             first_name text,
             last_name text,
             contact integer,
             email text,
             origin text,
             members integer
             )""")

        self.info_label = tk.Label(self.db_window,
                                   text="Please fill out the form below and We'll get back to you as soon as possible.")
        self.info_label.grid(row=1, columnspan=3, padx=20, pady=20)

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

        self.submit_btn = tk.Button(self.db_window, text='Add Record to Database', command=self.submit)
        self.submit_btn.grid(row=8, column=1, columnspan=2, padx=10, pady=10, ipadx=111)

        self.info_label = tk.Label(self.db_window, text="Other possibilities: ")
        self.info_label.grid(row=10, columnspan=3, padx=20, pady=20)

        self.id_box_label = tk.Label(self.db_window, text="Select ID")
        self.id_box_label.grid(row=12, column=1)

        self.id_box = tk.Entry(self.db_window, width=30)
        self.id_box.grid(row=12, column=2, pady=5)

        self.show_btn = tk.Button(self.db_window, text='Show Record', command=self.show)
        self.show_btn.grid(row=13, column=1, columnspan=2, padx=10, pady=10, ipadx=137)

        self.delete_btn = tk.Button(self.db_window, text='Delete Records', command=self.delete)
        self.delete_btn.grid(row=14, column=1, columnspan=2, padx=10, pady=10, ipadx=136)

        self.edit_btn = tk.Button(self.db_window, text='Edit Record', command=self.update)
        self.edit_btn.grid(row=15, column=1, columnspan=2, padx=10, pady=10, ipadx=146)

        self.conn.commit()
        self.db_window.mainloop()

    def update(self):
        try:
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

            self.id_box.delete(0, tk.END)
            self.f_name.delete(0, tk.END)
            self.l_name.delete(0, tk.END)
            self.contact.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.origin.delete(0, tk.END)
            self.members.delete(0, tk.END)

            messagebox.showinfo("Updated", "Record updated successfully !")
            self.conn.commit()
        except:
            pass

    def delete(self):
        try:
            self.c.execute("DELETE from detail WHERE oid= " + self.id_box.get())
            self.id_box.delete(0, tk.END)
            self.conn.commit()
            messagebox.showinfo("Deleted", "Record deleted successfully !")
        except:
            pass

    def submit(self):
        self.c.execute("INSERT INTO detail VALUES(:f_name, :l_name, :contact, :email, :origin, :members)",
                       {
                           'f_name': self.f_name.get(),
                           'l_name': self.l_name.get(),
                           'contact': self.contact.get(),
                           'email': self.email.get(),
                           'origin': self.origin.get(),
                           'members': self.members.get()
                       })

        self.f_name.delete(0, tk.END)
        self.l_name.delete(0, tk.END)
        self.contact.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.origin.delete(0, tk.END)
        self.members.delete(0, tk.END)

        messagebox.showinfo("Details saved", "We'll get back to you as soon as possible !")

        self.conn.commit()

    def show(self):
        try:
            self.c.execute('SELECT * FROM detail WHERE oid =' + self.id_box.get())
            records = self.c.fetchall()
            for record in records:
                self.f_name.insert(tk.END, record[0])
                self.l_name.insert(tk.END, record[1])
                self.contact.insert(tk.END, record[2])
                self.email.insert(tk.END, record[3])
                self.origin.insert(tk.END, record[4])
                self.members.insert(tk.END, record[5])

            self.id_box.delete(0, tk.END)
            self.conn.commit()
        except:
            pass

    def __del__(self):
        self.conn.close()
