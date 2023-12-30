#stepik_4.3_roulette_wheel_colors
print ("введите число")

a = int(input())

if a < 0 or a > 36:
    print ("ошибка ввода")

elif a == 0:
    print ("зеленый")

elif 1 <= a <= 10 or 19 <= a <= 28:
    if a%2==0:
        print ("черный")
    else:
        print ("красный")

elif 11 <= a <= 18 or 29 <= a <= 39:
    if a%2==0:
        print ("красный")
    else:
        print ("черный")

