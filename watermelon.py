weight = int(input("Enter the weight of the watermelon: "))
if weight %2 != 0 or weight == 2:
    print("Cannot be divided into two even parts")
else:
    pairs = []
    for first_part in range(2, weight//2 + 1, 2):
        second_part = weight - first_part
        if second_part % 2 == 0:
            pairs.append((first_part, second_part))
    print(pairs)