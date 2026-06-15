Param = {
    "name": "Param",
    "age": 17,
    "hobby" : "Guitar",
    "Favorite Color": "Blue",
    "Secondary Favorite Color": "Black",
    "Favourite Anime ": "Re:Zero",
    "Waifu": "Rem",

}
# no = int(input("Enter a number: "))
# till = int(input("Enter a number till which you want to print the table: "))
# for i in range(1, till+1):
#     print(f"{no} X {i}={no*i}")
star = "*"
layer  = int(input("Enter the number of layers: ")) + 2
space = " "
for i in range(1,layer+1):
    if i==1 or i==layer:
        print("*"*layer,end="")
        print("")
    else:
        print(star,end="")
        print(space*(layer-2),end="")
        print(star,end="")
        print("")
