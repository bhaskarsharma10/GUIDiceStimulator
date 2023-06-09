import random
import tkinter as tk
from PIL import Image, ImageTk

def roll_dice():
    dice_number = random.randint(1, 6)
    dice_image_path = f'dice_{dice_number}.png'
    dice_image = Image.open(dice_image_path)
    dice_photo = ImageTk.PhotoImage(dice_image, size='20*20')
    dice_label.config(image=dice_photo)
    dice_label.image = dice_photo

root = tk.Tk()
root.geometry('800x800')
root.title('GUI Dice Stimulator')
root.configure(bg='#f3f3f3')

l1 = tk.Label(root, text="Dice",
              fg="black", bg='#f3f3f3',
              font="helvetica 16 bold italic")
l1.pack()

dice_label = tk.Label(root, bg='#f3f3f3')
dice_label.pack()

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

root.mainloop()
