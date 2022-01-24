from tkinter import *

FONT = ('Arial', 12)

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

# Input entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text='Miles', font=FONT)
miles_label.grid(column=2, row=0)

equals_label = Label(text='is equal to')
equals_label.grid(column=0, row=1)

answer_label = Label(text='0', font=FONT)
answer_label.grid(column=1, row=1)

km_label = Label(text='Km', font=FONT)
km_label.grid(column=2, row=1)


# Buttons
def calculate():
    miles_number = float(miles_input.get())

    if miles_number == 1.0:
        miles_label.config(text='Mile')

    answer = miles_number * 1.60934
    answer_label.config(text=f'{answer}', font=FONT)


calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
