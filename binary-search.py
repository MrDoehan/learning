listed = [1, 2, 3, 4, 5, 6,]
target = 5
high = len(listed) - 1
low = 0
while low <= high:
    middle = (low + high) // 2
    if listed[middle] < target:
        low = middle+1
    elif listed[middle] > target:
        high = middle -1
    else:
        print(f"Target has been found at index {middle}")
        break