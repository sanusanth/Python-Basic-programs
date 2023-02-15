import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
// Creater By Sanusanth 
