f = open ("msg.txt", "r+")

print(f.read())


f.write("This is a new message added to the file.")
f.close()