import random 
alpha = 1.3
beta = 1.0
source_check = bool(int(input("Is Source Avaible ? (True = 1/False = 0): ")))
num_cell  = int(input("Enter the number of battery cells in battery pack: "))
if num_cell == 0 :
    print("Enter a Value Dammit!!")
else:
    pass
similar_cells = bool(int(input("Are all battery cells similar? (True = 1/False = 0): ")))
cells = { }
if not similar_cells:
    for i in range(num_cell):
        value  = float(input(f"Enter the Volatage capacity of Cell {i+1}: "))
        cells[i] = value
else:
    value = float(input("Enter the Volatage capacity of Cell: "))
    for i in range(num_cell):
        cells[i] = value
print(cells)
skewed_cell = { }
for i in range(num_cell):
    max_val = cells[i] + (cells[i]/100)*10
    min_val = cells[i] - (cells[i]/100)*40
    percentage = random.betavariate(alpha, beta)
    skewed_value = min_val + (max_val - min_val) * percentage
    
    skewed_cell[i] = skewed_value
for i in range(num_cell):
    overcharge = 5
    overdischarge = 30
    if skewed_cell[i] > cells[i] + (cells[i]/100)*overcharge:
        print(f"🔥 DANGER: Cell {i} is Over-Charged!")
    elif skewed_cell[i] < cells[i] - (cells[i]/100)*overdischarge:
        print(f"🔥 Warning: Cell {i} is Over-discharged!")
diffrence = max(skewed_cell.values()) - min(skewed_cell.values())
if  abs(diffrence) > 0.5 :
    print("⚖️ UNBALANCED: Pack needs balancing.")
more_info = bool(int(input("Do u Need more info? (True = 1/False = 0) : ")))