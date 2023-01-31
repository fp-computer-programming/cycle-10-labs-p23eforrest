nums = []
while True:
    num = int(input("input any number, and input -1 to end:"))
    if num == -1:
        break
    if num % 3 != 0:
        continue
    nums.append(num)
print("the numbers that you inputted that are multiples of 3 are", nums)