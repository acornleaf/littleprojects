# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400


year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print('Leap year.')
elif year % 100 == 0:
    print('Leap year.')
    if year % 400 == 0:
        print('Leap year.')
else:
        print('Not leap year.')