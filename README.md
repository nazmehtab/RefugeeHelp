
# Refugee Help Scheme

---
*A GUI application for Refugee database management support.*


## Description 

---
**The software is made to help refugees coming from different countries to Germany. It provides the following services:**
- Clothing & Fooding
- Lodging
- Social Services
- Others


## Requirements

---
**The repository is designed in Python programming language. The following dependencies are required to be installed:**

- Python >= 3.7 
- Tkinter (to create GUI)
- tkhtmlview (to create html view in tkinter)
- webbrowser (to open a webpage)
- PIL (to import Image and ImageTk)
- sqlite3 (to process database queries) 



## Files

---
- `README.md`
- `MainWindow.py`  Frontend interface of the software
- `info.py`  Information of different pages
- `DB.py`  Backend connection
- `details_book.db`  User's Database
- `Food.html`  Provide different service center locations
- `images`  This folder contains required images

	

## Database characteristics

---	
**details_book.db have the following fields:**
	
1. first_name: User's first name
2. last_name : User's last name
3. contact: User's contact number
4. email : User's email address
5. origin : User's country of origin
6. members : User's total family members
