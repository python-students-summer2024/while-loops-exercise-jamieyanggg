def get_starting_number():
    num_bottles = input("How many bottles of beer on the wall? ")
    if num_bottles.isnumeric():
        num_bottles = int(num_bottles)
        if num_bottles >= 1:
            return num_bottles
    return get_starting_number()

def sing(starting_number):
    for i in range(starting_number, 0, -1):
        if i > 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.\n")
        elif i == 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottle of beer on the wall.")
        elif i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")


