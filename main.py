from tkinter import *
from tkinter import messagebox 
import json
from password import Password
#-----------------------Search For The Data-----------------------#
def search():
    website=entry1.get().strip()
    data=None
    try:
        with open(r'C:\Users\anit4\OneDrive\Desktop\udemypy\GUI\tkinter\password manager\data.json','r') as file:
            data=json.load(file)
            messagebox.showinfo('Information',f'User : {data[website]['user']}\nPassword : {data[website]['password']}')
    except Exception as e:
        messagebox.showerror('Information','Data Not Found!')
#-----------------------Password Generate-------------------------#
def generate():
    my_password=Password().get()
    entry3.delete(0,END)
    entry3.insert(0,my_password)
#-----------------------store the data----------------------------#
def store():
    website=entry1.get().strip()
    user=entry2.get().strip()
    password=entry3.get().strip()
    if website and user and password:
        
        new_data={
            website:{
                'user':user,
                'password':password
            }
        }
        try:
            with open(r'C:\Users\anit4\OneDrive\Desktop\udemypy\GUI\tkinter\password manager\data.json','r') as file:
                data=json.load(file) #read the json data
                data.update(new_data) #update the json data
        except Exception as e:
            data=new_data
        finally:
            with open(r'C:\Users\anit4\OneDrive\Desktop\udemypy\GUI\tkinter\password manager\data.json','w') as file:
                json.dump(data,file,indent=4) #write the json data
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                messagebox.showinfo("Information", "Data Saved Successfully..")
    else:
        messagebox.showerror("Error", "Something Went Wrong Try Again!")
#-------------------------------ui----------------------------#

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#f7f5f2")

# Canvas for the logo
canvas = Canvas(width=200, height=200, bg="#f7f5f2", highlightthickness=0)
img = PhotoImage(file=r'C:\Users\anit4\OneDrive\Desktop\udemypy\GUI\tkinter\password manager\lock.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Website Label and Entry
text1 = Label(text="Website:", font=("Arial", 12, "bold"), bg="#f7f5f2", fg="#333")
text1.grid(row=1, column=0, pady=5, sticky="e")
entry1 = Entry(width=21, font=("Arial", 10))
entry1.focus()
entry1.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")
btn1 = Button(text="Search", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", borderwidth=0,command=search)
btn1.grid(row=1, column=2, pady=5, sticky="w")

# Email/Username/Number Label and Entry
text2 = Label(text="Email/Username/Number:", font=("Arial", 12, "bold"), bg="#f7f5f2", fg="#333")
text2.grid(row=2, column=0, pady=5, sticky="e")
entry2 = Entry(width=35, font=("Arial", 10))
entry2.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")


# Password Label and Entry
text3 = Label(text="Password:", font=("Arial", 12, "bold"), bg="#f7f5f2", fg="#333")
text3.grid(row=3, column=0, pady=5, sticky="e")
entry3 = Entry(width=21, font=("Arial", 10))
entry3.grid(row=3, column=1, pady=5, sticky="w")

# Generate Password Button
btn1 = Button(text="Generate Password", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", borderwidth=0,command=generate)
btn1.grid(row=3, column=2, pady=5, sticky="w")

# Add Button
btn2 = Button(text="Add", width=36, font=("Arial", 10, "bold"), bg="#2196F3", fg="white", borderwidth=0,command=store)
btn2.grid(row=4, column=1, columnspan=2, pady=20)


window.mainloop()
