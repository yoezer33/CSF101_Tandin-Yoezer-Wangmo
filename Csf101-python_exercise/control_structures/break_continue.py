for number in range(1, 10):
    if number == 5:
        break
    print(number)
for number in range(1, 6):
    if number == 3:
        continue
    print(number)  
count = 0
while True:
    count += 1
    if count == 3:
        continue
    if count == 5:
        break
    print(count)
print("Loop ended")
for i in range(5):
    print(i)
else:
    print("Loop completed normally")
n = 0
while n < 5:
    if n == 3:
        break
    print(n)
    n += 1
else:
    print("Loop completed normally")

print("Outside the loop")