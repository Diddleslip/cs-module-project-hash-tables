# Add up and print the sum of the all of the minimum elements of each inner array:
array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def adding_min_num(arr):
    total = 0

    for a in array:
        total += min(a)

    return total

print(adding_min_num(array))

