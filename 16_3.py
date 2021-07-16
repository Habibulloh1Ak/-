import random as rand
print("""Правила игры
Камень = 0
Ножницы = 1
Бумага = 2
0>1>2>0""")
while True:
    p1 = int(input("камень ножницы бумага"))
    p2 = rand.randint(0,2)
    if p1 == p2:
        print("Ничья")
    elif (p1 == 0 and p2 == 1) or(p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 0):
        print("Выиграл игрок")
    elif (p2 == 0 and p1 == 1) or(p2 == 1 and p1 == 2) or (p2 == 2 and p1 == 0):
        print("Выиграл компьютер")
    else:
        print("При таких условиях играть нельзя")
    end = int(input("Продолжите играть"))
    if not end:
        break
