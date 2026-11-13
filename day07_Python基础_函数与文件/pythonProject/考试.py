import random
count=0
list1 = []
total = 0
while count <= 10:
    num1 = random.randint(1, 30)
    list1.append(num1)
    count += 1
    for i in list1:
        if i % 2 == 1 and i % 3 == 0:
            total += i
print(total)


