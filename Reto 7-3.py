i : int
i = int(input("Ingrese un número mayor o igual a 2: "))
print("Lista descendente desde "+str(i)+" hasta 2")
while i >= 2:
    if i % 2 == 0:
        print(i)
    i -=1