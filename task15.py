age = int(input("Введите ваш возвраст: "))
for i in range(0, age+1):
    print(i)

if age % 2 == 0:
    for i in range(0, age+2):
        print(i)
else:
    for i in range(1, age+2):
        print(i)
