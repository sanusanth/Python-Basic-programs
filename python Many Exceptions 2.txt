#The try block will raise an error when trying to write to a read-only file:

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

#The program can continue, without leaving the file object open
