myNumber = int(input("What Number Would You Like To Test"))
count = 0
highNumber = 0
flag = myNumber%2

print(myNumber)
highNumber = myNumber
while myNumber > 1:
    flag = myNumber%2
    if flag == 0:
        myNumber = myNumber / 2
        print(myNumber, ", ")
        count += 1
    else:
        myNumber = (myNumber * 3) + 1
        print(myNumber, ", ")
        count += 1
    if myNumber > highNumber:
        highNumber = myNumber

print("It took", count, "steps")
print("The highest number was", highNumber)
