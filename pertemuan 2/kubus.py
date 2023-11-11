

import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    s = float((txtsisi.get()))

    L = round(6 * s + s )

    txtLuas.delete(0, END)
    txtLuas.insert(END, L)

def hitung_volume():
    s = float((txtsisi.get()))
  
    V = round(s * s * s )

    txtVolume.delete(0, END)
    txtVolume.insert(END, V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create
app = tk.Tk()
app.configure(bg="blue")

# Judul
app.title("Kalkulator Luas dan Volume Kubus")

# Windows
frame = Frame(app)
frame.pack (padx=20, pady=20)

# Label sisi
panjang = Label(frame, text="sisi : ")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox sisi
txtsisi = Entry(frame)
txtsisi.grid(row=0, column=1)


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