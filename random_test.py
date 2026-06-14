Param = {
    "name": "Param",
    "age": 17,
    "hobby" : "Guitar",
    "Favorite Color": "Blue",
    "Secondary Favorite Color": "Black",
    "Favourite Anime ": "Re:Zero",
    "Waifu": "Rem",

}
list = [ ]
for _ in range(4):
    num = int(input("Enter a number: "))
    list.append(num)
list.sort(reverse=True)
print(list[0])