f : int = 1
n : int
n = int(input("Ingrese un número del 2 al 50 para hallar sus divisores: "))
while n >= 2 and n <= 50 and f <= n : 
    if n % f == 0:
        print(str(f)+" es un número divisor de "+str(n))
    f+=1