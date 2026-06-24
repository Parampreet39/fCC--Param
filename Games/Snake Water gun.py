import random
# Swap the numbers to fix the math matrix
vals = {
    "Snake": 1,
    "Water": 3,
    "Gun": 2
}
computer = random.choice(list(vals.keys()))
player = input("Enter Your Choice -Snake-, -Water- or -Gun- : ")
if player in vals:
    player_num = vals[player]
else:
    print("Retry!!")
computer_num = vals[computer]
print(f"Computer Choose : {computer}")
result = player_num - computer_num
if result == 0 :
    print("TIE!")
elif result == 1 or result == -2:
    print("Player Wins!!🎉")
elif result == -1 or result == 2 :
    print("Computer Wins!!🤣🤣")