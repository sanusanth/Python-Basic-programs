txt = "Good night Sam!";

x = "mSa";
y = "eJo";
z = "odnght";

mytable = txt.maketrans(x, y, z);

print(txt.translate(mytable));
