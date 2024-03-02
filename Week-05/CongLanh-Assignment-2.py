# Assignment 2: Tkinter App
# Name: Cong Lanh Hoang
# Student ID: 301210743

# Import libraries
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Style

# Create inherited class from Tk
class Application(Tk):
  def __init__(self, title, geometry):
    Tk.__init__(self)
    self.programs = ["AI", "Gaming", "Health", "Software"]
    self.background_color = "#90EE90"

    self.title(title)
    self.geometry(geometry)
    self.configure(bg=self.background_color)

    # Create a frame to hold the widgets
    container = Frame(self, bg=self.background_color)
    container.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    
    self.create_ui(container)

  def create_ui(self, parent = None):
    if not parent: parent = self

    # Define grid layout
    parent.columnconfigure(list(range(3)), weight=1, uniform="a")
    parent.rowconfigure(list(range(9)), weight=0, uniform="a")

    # Create a label for the name of the data-entry form with bold & italic font
    heading_label = Label(parent, text="ICET Student Survey", font=("Calibri", 32, "bold", "italic"), bg=self.background_color)
    heading_label.grid(row=0, column=0, columnspan=3, sticky="new")

    # Create first column with the following labels
    full_name_label = Label(parent, text="Full Name:", font=("Calibri", 14), bg=self.background_color)
    full_name_label.grid(row=1, column=0, sticky="nw")

    residency_label = Label(parent, text="Residency:", font=("Calibri", 14), bg=self.background_color)
    residency_label.grid(row=2, column=0, sticky="nw")

    program_label = Label(parent, text="Program:", font=("Calibri", 14), bg=self.background_color)
    program_label.grid(row=4, column=0, sticky="nw")

    courses_label = Label(parent, text="Courses:", font=("Calibri", 14), bg=self.background_color)
    courses_label.grid(row=5, column=0, sticky="nw")

    # Create an entry that captures full name
    self.full_name = Entry(parent, font=("Calibri", 14))
    self.full_name.grid(row=1, column=1, sticky="nw")

    # Create residency radio buttons
    self.residency = StringVar()
    self.residency.set("dom")
    dom_radio = Radiobutton(parent, text="Domestic", variable=self.residency, value="dom", font=("Calibri", 14), bg=self.background_color)
    intl_radio = Radiobutton(parent, text="International", variable=self.residency, value="intl", font=("Calibri", 14), bg=self.background_color)
    dom_radio.grid(row=2, column=1, sticky="nw")
    intl_radio.grid(row=3, column=1, sticky="nw")

    # Create program combobox
    self.program = StringVar()
    self.program.set(self.programs[0])
    program_combobox = Combobox(parent, textvariable=self.program, values=self.programs, font=("Calibri", 14))
    program_combobox.grid(row=4, column=1, sticky="nw")

    # Create courses check buttons
    self.comp100 = StringVar()
    self.comp100.set("COMP100")
    comp100_check = Checkbutton(parent, text="Programming I", variable=self.comp100, onvalue="COMP100", offvalue="", font=("Calibri", 14), bg=self.background_color)
    comp100_check.grid(row=5, column=1, sticky="nw")

    self.comp213 = StringVar()
    self.comp213.set("")
    comp213_check = Checkbutton(parent, text="Web Page Design", variable=self.comp213, onvalue="COMP213", offvalue="", font=("Calibri", 14), bg=self.background_color)
    comp213_check.grid(row=6, column=1, sticky="nw")

    self.comp140 = StringVar()
    self.comp140.set("")
    comp140_check = Checkbutton(parent, text="Software Engineering", variable=self.comp140, onvalue="COMP140", offvalue="", font=("Calibri", 14), bg=self.background_color)
    comp140_check.grid(row=7, column=1, sticky="nw")

    # Create Reset button
    reset_button = Button(parent, text="Reset", command=self.reset, font=("Calibri", 14), highlightbackground=self.background_color)
    reset_button.grid(row=8, column=0, sticky="news", padx=5, pady=5)

    # Create OK button
    ok_button = Button(parent, text="OK", command=self.ok, font=("Calibri", 14), highlightbackground=self.background_color)
    ok_button.grid(row=8, column=1, sticky="news", padx=5, pady=5)

    # Create Exit button
    exit_button = Button(parent, text="Exit", command=self.exit, font=("Calibri", 14), highlightbackground=self.background_color)
    exit_button.grid(row=8, column=2, sticky="news", padx=5, pady=5)

  def reset(self):
    self.full_name.delete(0, END)
    self.residency.set("domestic")
    self.program.set(self.programs[0])
    # uncheck the check buttons
    self.comp100.set("COMP100")
    self.comp213.set("")
    self.comp140.set("")
  
  def ok(self):
    message = f"{self.full_name.get()}\n{self.program.get()}\n{self.residency.get()}\n" \
      f"({self.comp100.get()} {self.comp213.get()} {self.comp140.get()})"
    messagebox.showinfo("Information", message)

  def exit(self):
    self.destroy()

if __name__ == "__main__":
  app = Application("Centennial College", "640x480")
  app.mainloop()