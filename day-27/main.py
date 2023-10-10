from tkinter import *


# Button
def miles_to_km():
    miles = int(input_miles.get())
    km = round(miles * 1.609)
    label_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# row 0
input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)

label_miles = Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=2, row=0)

# row 1
label_is_equal_to = Label(text="is equal to", font=("Arial", 12))
label_is_equal_to.grid(column=0, row=1)

label_result = Label(text="0", font=("Arial", 12))
label_result.grid(column=1, row=1)

label_km = Label(text="Km", font=("Arial", 12))
label_km.grid(column=2, row=1)

# row 2
button_calculate = Button(text="Calculate", command=miles_to_km)
button_calculate.grid(column=1, row=2)

# 마지막
window.mainloop()
