#!C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe

import cgi

def sum_of_digits(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum

form = cgi.FieldStorage()
number = int(form.getvalue("number"))

print("Content-type:text/html\r\n\r\n")
print(f"<html><head><title>Sum of Digits</title></head><body>")
print(f"<h1>The sum of digits in {number} is {sum_of_digits(number)}.</h1>")
print("</body></html>")
