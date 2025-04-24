first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first != second and first != third and second != third:
    print("Число совпадений: 0")

elif first != second or first != third or third != second:
    print("Число совпадений: 2")

else:
    first == second == third
    print("Число совпадений: 3")
