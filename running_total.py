number = int(input("number please"))

sum = 0

while number >= 1:
    sum = (number + sum)
    number = int(input("number please"))

print(sum)