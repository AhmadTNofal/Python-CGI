#!C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe

import cgi
import random

def dice_rolling_game(num_dice, max_value, num_tries):
    best_sum = 0
    for _ in range(num_tries):
        dice_sum = sum(random.randint(1, max_value) for _ in range(num_dice))
        best_sum = max(best_sum, dice_sum)
    
    return best_sum

form = cgi.FieldStorage()
num_dice = int(form.getvalue("num_dice"))
max_value = int(form.getvalue("max_value"))
num_tries = int(form.getvalue("num_tries"))

best_sum = dice_rolling_game(num_dice, max_value, num_tries)

print("Content-type:text/html\r\n\r\n")
print(f"<html><head><title>Dice Rolling Game</title></head><body>")
print(f"<h1>Best sum after {num_tries} tries: {best_sum}</h1>")
print("</body></html>")
