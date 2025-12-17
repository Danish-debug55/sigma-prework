def find_low_high(numbers):
    # start by assuming the first element is both lowest and highest
    lowest = numbers[0]
    highest = numbers[0]

    # loop through the list and update lowest and highest value when needed
    for num in numbers:
        if num < lowest:
            lowest = num
        if num > highest:
            highest = num

    return [lowest, highest]


print(find_low_high([2, 4, 1, 0, 2, -1]))      # expected [-1, 4]
print(find_low_high([20, 50, 12, 6, 14, 8]))   # expected [6, 50]
print(find_low_high([100, -100]))              # expected [-100, 100]
