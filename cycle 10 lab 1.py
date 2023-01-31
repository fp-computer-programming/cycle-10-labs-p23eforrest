sum = 0
while True:
    num = int(input("Enter a number, enter -1 to end :"))
    if num == -1:
        break
    sum += num
print("Sum:", sum)