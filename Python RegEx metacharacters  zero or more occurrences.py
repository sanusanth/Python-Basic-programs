import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
// Creater By Sanusanth
