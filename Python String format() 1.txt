#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "sanu", age = 24)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("sannu",24)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("sanu",24)

print(txt1)
print(txt2)
print(txt3)
