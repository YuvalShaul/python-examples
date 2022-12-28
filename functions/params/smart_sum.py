
def sum_all(*numbers):
    sum=0
    print(type(numbers))
    for num in numbers:
        sum += num
    print(sum)


sum_all(6, 7, 8)
sum_all(6, 7, 8, 4, 6,8,6, 3, 65, 8, 9)



