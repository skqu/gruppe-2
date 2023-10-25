#importerer TKinter
from tkinter import *


# GUI for lommeregneren vi laver
#Laver roden for lommeregneren, med en title og størelsen for hvor man kan skrive
root = Tk()
root.title("Lommeregner 2.0")
root.geometry("320x345")
root.resizable(False, False)
root.configure(bg="#444547")
e = Entry(root, width=20, borderwidth=1,bg="#666769", fg="white", font=("Helvetica", 16))
e.grid(row=0, column=0, columnspan=100, padx=(10, 10), pady=10)

#Sørger for at man kun kan skrive numre i den
def is_valid_input(P):
    return (P.isdigit() or P in "+-*÷") and not (e.get() == "" and P in "+-*÷")

vcmd = root.register(is_valid_input)
e.configure(validate="key", validatecommand=(vcmd, "%P"))

def button_click(char):
    if char == 'C':
        e.delete(0, END)
    elif char == '=':
        try:
            current_text = e.get()
            current_text = current_text.replace("÷", "/").replace("*", "*")
            result = eval(current_text)
            e.delete(0, END)
            e.insert(END, result)
        except:
            e.delete(0, END)
            e.insert(END, "Error")
    else:
        current_text = e.get()
        # Check if there's an error message; if so, clear it
        if current_text == "Error":
            current_text = ""
        e.delete(0, END)
        e.insert(END, current_text + str(char))

def button_clear():
    e.delete(0, END)

button_font = ("Arial", 16, "bold")


#Tal
button_1 = Button(root, text="1", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(1))
button_2 = Button(root, text="2", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(2))
button_3 = Button(root, text="3", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(3))
button_4 = Button(root, text="4", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(4))
button_5 = Button(root, text="5", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(5))
button_6 = Button(root, text="6", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(6))
button_7 = Button(root, text="7", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(7))
button_8 = Button(root, text="8", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(8))
button_9 = Button(root, text="9", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(9))
button_0 = Button(root, text="0", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769", fg="white", command=lambda: button_click(0))

#placering
button_1.grid(row=1, column=0, padx=(10, 1), pady=1)
button_2.grid(row=1, column=1, padx=1, pady=1)
button_3.grid(row=1, column=2, padx=1, pady=1)
button_4.grid(row=2, column=0, padx=(10, 1), pady=1)
button_5.grid(row=2, column=1, padx=1, pady=1)
button_6.grid(row=2, column=2, padx=1, pady=1)
button_7.grid(row=3, column=0, padx=(10, 1), pady=1)
button_8.grid(row=3, column=1, padx=1, pady=1)
button_9.grid(row=3, column=2, padx=1, pady=1)
button_0.grid(row=4, column=1, padx=1, pady=1)

#Lig med og slet
button_clear = Button(root, text="C", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769",fg="white", command=button_clear)
button_equal = Button(root, text="=", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769",fg="white", command=lambda: button_click("="))

#placering
button_clear.grid(row=4, column=0, padx=(10, 1), pady=1)
button_equal.grid(row=4, column=2, padx=1, pady=1)

#plus, minus, division og gange
button_addition = Button(root, text="+", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769",fg="white", command=lambda: button_click("+"))
button_subtraction = Button(root, text="-", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769",fg="white", command=lambda: button_click("-"))
button_multiply = Button(root, text="*", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769",fg="white", command=lambda: button_click("*"))
button_division = Button(root, text="÷", font=button_font, width=2, height=1, padx=20, pady=15,bg="#666769",fg="white", command=lambda: button_click("÷"))

#placering
button_addition.grid(row=1, column=4, padx=1, pady=1)
button_subtraction.grid(row=2, column=4, padx=1, pady=1)
button_multiply.grid(row=3, column=4, padx=1, pady=1)
button_division.grid(row=4, column=4, padx=1, pady=1)

root.mainloop()