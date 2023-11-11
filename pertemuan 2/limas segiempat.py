

import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    a = float((txtalas.get()))
    t = float((txttinggi.get()))
    s = float((txtsisi.get()))
    L = round((a *t/2)*4 + (s * s))

    txtLuas.delete(0, END)
    txtLuas.insert(END, L)

def hitung_volume():
    a = float((txtalas.get()))
    t = float((txttinggi.get()))
    s = float((txtsisi.get()))
    V = round(1/3 * (s*s)* t)

    txtVolume.delete(0, END)
    txtVolume.insert(END, V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create
app = tk.Tk()
app.configure(bg="brown")

# Judul
app.title("Kalkulator Luas dan Volume limas segiempat")

# Windows
frame = Frame(app)
frame.pack (padx=20, pady=20)

# Label alas
alas = Label(frame, text="alas :")
alas.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Panjang
txtalas = Entry(frame)
txtalas.grid(row=0, column=1)

# Label tinggi
tinggi = Label(frame, text="tinggi :")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=1, column=1)

# Label sisi
sisi = Label(frame, text="sisi :")
sisi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txtsisi = Entry(frame)
txtsisi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas= Label(frame, text="Luas:" )
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1)

# Output Volume
volume= Label(frame, text="Volume:" )
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)
#  Textbox Volume 
txtVolume = Entry(frame)
txtVolume.grid(row=5, column=1)

app.mainloop()