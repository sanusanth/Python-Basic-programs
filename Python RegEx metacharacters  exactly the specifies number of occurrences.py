import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "a" followed by exactly two "l" characters:

x = re.findall("al{2}", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
// Creater By Sanusanth 
