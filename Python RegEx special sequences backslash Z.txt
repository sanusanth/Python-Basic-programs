import re

txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
