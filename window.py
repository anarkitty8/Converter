from tkinter import *
import customtkinter as ctk
import utilities

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

Window = ctk.CTk()
Window.geometry("500x300")
Window.resizable(width=False, height=False)
Window.title("Converter")

user_input = StringVar(Window)
user_output = StringVar(Window)


def button_clicked():
    if input_type.get() == "Number":
        try:
            user_output.set(utilities.convert_from_int(int(input_entry.get()), output_type.get()))
        except ValueError:
            user_output.set("Invalid Input")
    elif input_type.get().strip() == "Text":
        try:
            user_output.set(utilities.convert_from_text(input_entry.get(), output_type.get()))
        except ValueError:
            user_output.set("Invalid Input")
    elif input_type.get() == "Hex":
        try:
            user_output.set(utilities.convert_from_hex(input_entry.get(), output_type.get()))
        except ValueError:
            user_output.set("Invalid Input")
    elif input_type.get() == "Binary":
        try:
            user_output.set(utilities.convert_from_binary(input_entry.get(), output_type.get()))
        except ValueError:
            user_output.set("Invalid Input")


input_entry = ctk.CTkEntry(master=Window, placeholder_text="Input", textvariable=user_input)
input_entry.place(relx=0.2, rely=0.35, anchor=ctk.CENTER)

input_type = ctk.CTkComboBox(master=Window, values=["Base64", "Binary", "Hex", "Number", "Text"])
input_type.place(relx=0.2, rely=0.2, anchor=ctk.CENTER)

output_entry = ctk.CTkLabel(master=Window, textvariable=user_output)
output_entry.place(relx=0.7, rely=0.35, anchor=ctk.CENTER)

output_type = ctk.CTkComboBox(master=Window, values=["Base64", "Binary", "Hex", "Number", "Text"])
output_type.place(relx=0.8, rely=0.2, anchor=ctk.CENTER)

calculate = ctk.CTkButton(master=Window, text="Convert", command=button_clicked)
calculate.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

Window.mainloop()
