i : int = 1
n : int
n = int(input("Ingrese el número natural: "))
while n > 0:
    i = i *n
    n -=1
print ("El factorial del número ingresado es: "+str(i))