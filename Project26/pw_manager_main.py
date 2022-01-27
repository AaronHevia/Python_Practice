from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


EMAIL = 'email.com'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()

    try:
        with open('./password_manager.json', 'r') as manager:
            # Read Data in Manager
            data = json.load(manager)
    except FileNotFoundError:
        messagebox.showinfo(title='Error',
                            message='Password Manager not found.  Create one by adding a new entry.')
    else:
        if website in data:
            username = data[website]["Username/Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=f'{website} Info',
                                message=f'Website:  {website}\n'
                                        f'Username/Email: {username}\n'
                                        f'Password:  {password}')

        messagebox.showinfo(title=f'{website} Not Found',
                            message=f'There is no history for the website you are looking for.')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_entry = {
        website: {
            'Username/Email': username,
            'Password': password
        }
    }

    # Ensure there is data to save.
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title='Empty Field Entry', message='Fields cannot be empty.  Try again.')
    else:
        # Verify entry is correct.
        ok = messagebox.askokcancel(title=f'{website} Verification',
                                    message=f'These are the details entered:\n'
                                            f'Website:  {website}\n'
                                            f'Username/Email:  {username}\n'
                                            f'Password:  {password}\n'
                                            f'Press OK to save or Cancel to edit.')

        if ok:
            try:
                with open('./password_manager.json', 'r') as manager:
                    # Read Data in Manager
                    data = json.load(manager)
            except FileNotFoundError:
                with open('./password_manager.json', 'w') as manager:
                    # Save/Write first Data to Manager
                    json.dump(new_entry, manager, indent=4)
            else:
                # Update Data to Save
                data.update(new_entry)
                # Save/Write Data to Manager
                with open('./password_manager.json', 'w') as manager:
                    json.dump(data, manager, indent=4)
            finally:
                # Delete all info and set username to default value if it was changed.
                entries = [website_entry, username_entry, password_entry]
                for entry in entries:
                    entry.delete(0, END)
                    if entry == username_entry:
                        entry.insert(0, EMAIL)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', anchor='e')
website_label.grid(column=0, row=1, pady=5)

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, pady=5)
website_entry.focus()

search_button = Button(width=15, text='Search', command=search)
search_button.grid(column=2, row=1, pady=5)

username_label = Label(text='Email/Username:', anchor='e')
username_label.grid(column=0, row=2, pady=5)

username_entry = Entry(width=52)
username_entry.grid(column=1, row=2, pady=5, columnspan=2)
username_entry.insert(0, EMAIL)

password_label = Label(text='Password:', anchor='e')
password_label.grid(column=0, row=3, pady=5)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, pady=5)

generate_button = Button(width=15, text='Generate Password', command=generator)
generate_button.grid(column=2, row=3, pady=5)

add_button = Button(width=44, text='Add', command=save)
add_button.grid(column=1, row=4, pady=5, columnspan=2)


def main():
    window.mainloop()


if __name__ == '__main__':
    main()
