def calcularPrimos(n:float):
    n = 1
    while n <= 100:
        f = 0
        i = 1
        while i <= n:
            if n % i == 0:
                f +=1
            i +=1
        if f == 2:
            print(n)
        n +=1
if __name__=="__main__":
    print("Los números primos son:")
    primos = calcularPrimos(n)
    print(str(primos))
