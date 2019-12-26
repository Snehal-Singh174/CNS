alphabet='abcdefghijklmnopqrstuvwxyz'
newtext=""
newdec=""

text=input("Enter the text : ")
key=int(input("Enter key: "))
for character in text:
    position=alphabet.find(character)
    n=(position+key) % 26
    c=alphabet[n]
    newtext+=c
print("Encrypted Text : "+newtext)


for character in newtext:
    position=alphabet.find(character)
    no=(position-key) % 26
    ce=alphabet[no]
    newdec+=ce
print("Decrypted Text : "+newdec)
