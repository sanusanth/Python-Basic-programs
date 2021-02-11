#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars."
print(txt.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = "The price is {:f} dollars."
print(txt.format(45))
