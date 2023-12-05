filename = "input2.txt"
with open(filename) as file:
    input = [line.rstrip() for line in file]

# Part 1
total1 = 0

for index, game in enumerate(input, 1):
    possible = True
    words = game.split()[2:]
    for num, colour in zip(words[::2], words[1::2]):
        num = int(num)
        if (
            (colour[0] == "r" and num > 12)
            or (colour[0] == "g" and num > 13)
            or (colour[0] == "b" and num > 14)
        ):
            possible = False
    if possible:
        total1 += index

print(total1)

# Part 2

total2 = 0

for index, game in enumerate(input, 1):
    min_red, min_green, min_blue = 0, 0, 0
    words = game.split()[2:]
    for num, colour in zip(words[::2], words[1::2]):
        num = int(num)
        if colour[0] == "r" and num > min_red:
            min_red = num
        if colour[0] == "g" and num > min_green:
            min_green = num
        if colour[0] == "b" and num > min_blue:
            min_blue = num
    power = min_red * min_green * min_blue
    total2 += power

print(total2)
