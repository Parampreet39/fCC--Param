Param = {
    "name": "Param",
    "age": 17,
    "hobby" : "Guitar",
    "Favorite Color": "Blue",
    "Secondary Favorite Color": "Black",
    "Favourite Anime ": "Re:Zero",
    "Waifu": "Rem",

}
def greatest(a,b,c):
    no = [a,b,c]
    result = sorted(no,reverse=True)
    print(sorted)
    print(f"Greatest no. is {result[0]}")
def sum_numbers(n):
    if n == 1:
        return 1  
    return n + sum_numbers(n - 1)  
def pattern(n):
    if n==1:
        print("*")
        return 
    if n != 0:
        print(n*"*")
        pattern(n-1)
        return 
    return
def pattern(n):
    if n == 0:
        return
        
    pattern(n - 1)  # 👈 Call first (goes down to 0)
    print(n * "*")  # 👈 Print last (prints on the way back up)

pattern(4)

"""
*
**
***
"""