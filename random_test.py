Param = {
    "name": "Param",
    "age": 17,
    "hobby" : "Guitar",
    "Favorite Color": "Blue",
    "Secondary Favorite Color": "Black",
    "Favourite Anime ": "Re:Zero",
    "Waifu": "Rem",

}
"""
Python I/O
"""
x = open("File.txt")
message = x.read()
print(message)
y = open("File.txt", "w")
name = input("Enter Your name")
new_message = name
y.write(new_message)
print(y)
y.close()