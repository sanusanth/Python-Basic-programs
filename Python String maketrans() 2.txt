txt = "Hi Sam!";

x = "mSa";
y = "eJo";

mytable = txt.maketrans(x, y);

print(txt.translate(mytable));
