
number = 16


for divider in range(2, number):
    if (number % divider) == 0:
        print("Not prime")
        break
else:
    print("Prime")


print("after")
