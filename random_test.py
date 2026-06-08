Param = {
    "name": "Param",
    "age": 17,
    "hobby" : "Guitar",
    "Favorite Color": "Blue",
    "Secondary Favorite Color": "Black",
    "Favourite Anime ": "Re:Zero",
    "Waifu": "Rem",

}
dict = {}
for _ in range(4):
    Name = input("What is your name? ")
    Language = input("What is your favorite programming language? ")
    dict.update({Name: Language})


print(dict, type(dict))