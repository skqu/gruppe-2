# Importerer tkinter-modulet og giver det et alias 'tk' for nem adgang
import tkinter as tk

# Funktion til at håndtere knaptryk og udføre beregninger
def calculate(event):
    # Henter teksten på den knap, der blev klikket på
    text = event.widget.cget("text")
    
    # Hvis knappen er "=", udfør følgende
    if text == "=":
        try:
            # Evaluerer og konverterer resultatet til en streng og opdaterer skærmen
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            # Hvis der opstår en fejl, vis "Fejl" på skærmen
            screen.set("Fejl")
    
    # Hvis knappen er "C", ryd skærmen
    elif text == "C":
        screen.set("")
    
    # Hvis knappen er "⌫", fjern den sidste karakter på skærmen
    elif text == "⌫":
        screen.set(screen.get()[:-1])
    
    # For alle andre knapper, tilføj deres tekst til skærmen
    else:
        screen.set(screen.get() + text)

# Opret hovedvinduet
root = tk.Tk()

# Indstil størrelsen på hovedvinduet
root.geometry("300x400")

# Indstil titlen på hovedvinduet
root.title("Lommeregner")

# Opret en StringVar til at holde skærmindeholdet
screen = tk.StringVar()

# Opret et indtastningsfelt (Entry-widget) og tilknyt det til skærmen
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")

# Placer indtastningsfeltet i række 0, kolonne 0 og stræk det over 4 kolonner
entry.grid(row=0, column=0, columnspan=4)

# Definer knapgrupper til lommeregneren
buttons = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/'],
    ['C', '⌫']
]

# Opret knapper og bind dem til calculate-funktionen
# Løkke gennem 5 iterationer for rækker i grænsefladen
for i in range(5):

    # Løkke gennem elementerne i den aktuelle række
    for j in range(len(buttons[i])):

        # Opret en knap med specificeret tekst og skrifttype
        btn = tk.Button(root, text=buttons[i][j], font='lucida 15 bold')

        # Bind begivenhedshåndtereren "calculate" til venstreklik på knappen
        btn.bind("<Button-1>", calculate)

        # Placer knappen i gitteret på den rigtige række og kolonne
        btn.grid(row=i+1, column=j)

# Start hovedløkken for tkinter
root.mainloop()
