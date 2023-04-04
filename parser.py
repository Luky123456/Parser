import tkinter as tk
import PyPDF4
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 300)
canvas.grid(columnspan = 3, rowspan = 3) #spravi to 3 identicke rovnomerne stlpy

#vytvorenie loga
logo = Image.open("logodu.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = tk.Label(image=logo)
logoLabel.image = logo
logoLabel.grid(column = 1, row = 0)

#instrukcie pre program
instructions = tk.Label(root, text = "Vyber si PDF súbor na svojom pocítači na vytrhnutie textu z neho", font = "Ariel")
instructions.grid(columnspan = 3, column = 0, row = 1)

def open_file(): #funkcia ktora bude otvarat subory
    browse_text.set("Načítavanie...")
    file = askopenfile(parent = root, mode = "rb", title = "Vyber si súbor", filetype = [("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF4.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        #text
        text_box = tk.Text(root, height = 10, width = 50, padx = 15, pady = 15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify = "center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column = 1, row = 3)

        browse_text.set("Prehliadaj")

#tlacitko na prehladanie suborov
browse_text = tk.StringVar()
browse_button = tk.Button(root, textvariable = browse_text, command = lambda:open_file(), bg="turquoise", fg="white", height = 2, width = 20)
browse_text.set("Prehliadaj")
browse_button.grid(column = 1, row = 2)

canvas = tk.Canvas(root, width = 600, height = 250)
canvas.grid(columnspan = 3)

root.mainloop()
