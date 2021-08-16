'''creating a GUI based  BMI calculator project'''

from tkinter import *           # importing all the required elements
from handling import *          # importing classes created in handling file
from tkinter import messagebox

# initializing the global constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f9f871"
BLUE = "#a3ddcb"
YELLOW_ORANGE ="#f0a500"

# window 
window = Tk()          
window.title("Body Mass Index - Calculator")
window.config(bg=GREEN, padx=50, pady=50)
icon_photo = PhotoImage(file="bmi_img.png")        # using custom icon 
window.iconphoto(False, icon_photo)
window.geometry("800x510")
window.resizable(0, 0)         # setting window fixed


# BMI label
b_label = Label(text="BMI Calculator", font=("Algerian", 30, 'underline'))
b_label.config(padx=5, pady=0, bg=GREEN)
b_label.grid(row=1, column=1, columnspan=2)

# mass entry field
mass_label = Label(text="Mass Field", font=("Courier", 20, "bold"))
mass_label.grid(row=2, column=2)

# unit picker for mass
choose_mass_unit = Label(text="Choose Unit for Mass ", font=("Comic Sans Ms", 10, "bold"), width=24, bg=YELLOW)
choose_mass_unit.grid(row=3, column=0)

# user's mass entry filed
mass_entry = Entry(width=15)
mass_entry.grid(row=3, column=3)

# Variable to hold on to which radio button value is checked.
mass_unit = StringVar()
radiobutton1 = Radiobutton(text="kg", value="kg", variable=mass_unit)
radiobutton2 = Radiobutton(text="pound", value="pound", variable=mass_unit)
radiobutton1.grid(row=4, column=0)
radiobutton2.grid(row=5, column=0)



# height field
height_label = Label(text="Height Field",  font=("Courier" , 20, "bold"))
height_label.grid(row=6, column=2)

# unit picker for height
choose_height_unit = Label(text="Choose Unit for Height", font=("Comic Sans Ms", 10, "bold"), width=24, bg=YELLOW)
choose_height_unit.grid(row=7, column=0)

# height entry
height_entry = Entry(width=15)
height_entry.grid(row=7, column=3)

# Variable to hold on to which radio button value is checked.
height_unit = StringVar()
radiobutton3 = Radiobutton(text="Meter", value="m", variable=height_unit)
radiobutton4 = Radiobutton(text="Centi Meter", value="cm", variable=height_unit)
radiobutton5 = Radiobutton(text="Feet", value="feet", variable=height_unit)
radiobutton6 = Radiobutton(text="Inches", value="inch", variable=height_unit)
radiobutton3.grid(row=8, column=0)
radiobutton4.grid(row=9, column=0)
radiobutton5.grid(row=10, column=0)
radiobutton6.grid(row=11, column=0)


# defining command to do when "check bmi" button is pressed
def submit_action():
    if len(mass_entry.get())==0 or len(height_entry.get())==0:
        messagebox.showwarning(title="Empty Fields", message="Plese Don't leave any fields empty. ")

    elif float(mass_entry.get()) <=0 or float(height_entry.get()) <=0:
        messagebox.showerror(title="Invalid Entries", message="Height or Weight can't be less than or equal to zero. ")
    
    else:
        user_mass = MassHandler(mass=float(mass_entry.get()), unit=mass_unit.get())
        user_height = HeightHandler(height=float(height_entry.get()), unit=height_unit.get())
        user_mass.unit_convert()
        user_height.unit_converter()
        user_bmi = BmiHandler(mass=user_mass.mass, height=user_height.height)
        result_label.config(text=f"Your BMI is {user_bmi.bmi_value():1.2f}")
        remark_label.config(text=f"{user_bmi.check_range()}")


submit_button = Button(text="Check BMI", command=submit_action, font=("comic sans ms", 10, "bold"))
submit_button.grid(row=12, column=2)
submit_button.config(bg="#fddb3a", activebackground="#cdb30c", relief="ridge", cursor="hand2")

result_label = Label(text=f"BMI will be displayed here")
result_label.grid(row=13, column=2)

remark_label = Label(text="Remarks will be shown here")
remark_label.grid(row=14, column=2)


# configuring required elements all at once
for label in [height_label, mass_label]:
    label.config(bg="#ffc75f", width=13)

for radiobuttons in [radiobutton1, radiobutton2, radiobutton3, radiobutton4, radiobutton5, radiobutton6]:
    radiobuttons.config(bg=BLUE, width=20, anchor="w", activebackground="#487e95", relief="groove", cursor="hand2")

for item in [result_label, remark_label]:
    item.config(width=45, relief='groove', bg="#b6eb7a")



window.mainloop()
