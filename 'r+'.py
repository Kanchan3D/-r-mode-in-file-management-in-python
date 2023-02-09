f=open("text.txt",'r+')

f.write("sanb")
f.seek(10)
print(f.tell())
text=f.read()
print(text)
f.close()