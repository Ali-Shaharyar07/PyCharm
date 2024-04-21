nums = [5]
target = -5

lower = 0
upper = len(nums) - 1
middle = int((upper + lower) / 2)

#print("lower: ", lower, " middle: ", middle, "upper: ", upper)

while True:
    if nums[middle] < target:
        lower = middle
        middle = int((upper + lower) / 2)
        print("lower: ", lower, " middle: ", middle, "upper: ", upper)
    elif nums[middle] > target:
        upper = middle
        middle = int((upper + lower) / 2)
        print("lower: ", lower, " middle: ", middle, "upper: ", upper)
    elif nums[middle] == target:
        print(middle)
    else:
        print(-1)

    if upper-lower == 1  or upper == lower:
        print(-1)


