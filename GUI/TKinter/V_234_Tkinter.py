import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("GUI")

# Create Labels
name_label = ttk.Label(win, text="Enter your name: ")
name_label.grid(row=0, column=0, sticky=tk.W)  # W --> West side of the window(to start writing from left)

age_label = ttk.Label(win, text="Enter your age: ")
age_label.grid(row=1, column=0, sticky=tk.W)

email_label = ttk.Label(win, text="Enter your e-mail: ")
email_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text="Gender: ")
gender_label.grid(row=3, column=0, sticky=tk.W)

role_label = ttk.Label(win, text="choose your profession: ")
role_label.grid(row=4, column=0, sticky=tk.W)

# Create Entry Box for input
name_var = tk.StringVar()  # variable for storing the name through user
name_input = ttk.Entry(win, width=16, textvariable=name_var)  # text-variable is assigning the variable
name_input.grid(row=0, column=1)
name_input.focus()  # by default the cursor will here

age_var = tk.IntVar()
age_input = ttk.Entry(win, width=16, textvariable=age_var)
age_input.grid(row=1, column=1)

email_var = tk.StringVar()
email_input = ttk.Entry(win, width=16, textvariable=email_var)
email_input.grid(row=2, column=1)

# Create combo-box (drop-down menu)
gender_var = tk.StringVar()
gender_cbox = ttk.Combobox(win, width=14, textvariable=gender_var, state="readonly")
# using 'readonly' state user can't type anything in the combobox.
gender_cbox['values'] = ("Male", "Female", "Other")
gender_cbox.current(0)  # by default ---> 0 means 0th index of the tuple(drop menu options) i.e. male already selected
gender_cbox.grid(row=3, column=1)

# Creating Radio button
role_var = tk.StringVar()

radio_btn = ttk.Radiobutton(win, text="student", value="student", variable=role_var)
radio_btn.grid(row=4, column=1)
# value--> student/professor will store in the variable role_var
radio_btn2 = ttk.Radiobutton(win, text="professor", value="professor", variable=role_var)
radio_btn2.grid(row=4, column=2)

radio_btn3 = ttk.Radiobutton(win, text="staff", value="staff", variable=role_var)
radio_btn3.grid(row=4, column=3)

radio_btn4 = ttk.Radiobutton(win, text="other", value="other", variable=role_var)
radio_btn4.grid(row=4, column=4)

# Creating a checkBox
checkbox = tk.IntVar()
check_box1 = ttk.Checkbutton(win, text="i am assuring that the above info is correct.", variable=checkbox)
check_box1.grid(row=6, columnspan=3, sticky=tk.W)

try:
    # Button
    def button_action():
        print(type(age_var.get()))
        if not checkbox.get():
            ttk.Label(win, text="check the box!").grid(row=7, columnspan=3)

        elif type(age_var.get()) == int:
            ttk.Label(win, width=17).grid(row=7, columnspan=3)
            name = name_var.get()
            age = age_var.get()
            gender = gender_var.get()
            email = email_var.get()
            role = role_var.get()

            print(f"your name is {name}")
            print(f"you are {age} years old")
            print(f"you are {gender}")
            print(f"your e-mail id is {email}")
            print(f"you are a {role}")

            with open("user_data.txt", 'a') as f:
                f.write(f"username: {name}, age: {age}, sex: {gender}, e-mail: {email}, profession: {role}\n")
                f.close()
                name_input.delete(0, tk.END)
                age_input.delete(0, tk.END)
                email_input.delete(0, tk.END)
        else:
            ttk.Label(win, text="  Invalid age!  ").grid(row=7, columnspan=3)


    # command will execute those function which is going to perform after clicking on submit button
    submit_button = ttk.Button(win, text="Submit", command=button_action)
    submit_button.grid(row=7, column=0)


except():
    print("something went wrong!")
# avoid auto-exit of the window
win.mainloop()
