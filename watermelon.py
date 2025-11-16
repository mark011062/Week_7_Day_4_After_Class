weight = int(input("Enter the weight of the watermelon: "))
if weight %2 != 0 or weight == 2:
    print("NO")
else:
    pairs = []
    for first_part in range(2, weight//2 + 1, 2): #this ensures first_part is even, gets the weight divided by 2, and only checks even numbers
        second_part = weight - first_part
        if second_part % 2 == 0: # this checks to see if the second part is even
            pairs.append((first_part, second_part))
    print("YES")        
    