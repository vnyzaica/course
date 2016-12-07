
f = open("8.py")
print(f.read(100))
print(f.read(100))

f.seek(0)
print(f.read(100))

for line in f:
    print("line: ",line.strip())#strip or rstrip