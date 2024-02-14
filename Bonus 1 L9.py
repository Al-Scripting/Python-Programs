#Muqshith Shifan 100862739
import tkinter as tk
import random

# Define the window
window = tk.Tk()
window.title("Tic Tac Toe")

# Define the images for X and O
x_image = tk.PhotoImage(file="x.gif")
o_image = tk.PhotoImage(file="o.gif")

# Create the labels for the board
labels = []
for row in range(3):
    for col in range(3):
        label = tk.Label(window, image=None)
        label.grid(row=row, column=col)
        labels.append(label)

# Randomly set X's and O's on the board
for label in labels:
    if random.randint(0, 1) == 0:
        label.config(image=x_image)
    else:
        label.config(image=o_image)

# Run the window
window.mainloop()
