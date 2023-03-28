n : int = 50
p = input("¿50 es tu número?, pon sí(sï es igual), mayor(sí tu número es mayor que 50) o menor (sí tu número es menor a que 50): ")
while p != "sí":
    if p == "menor":
        n-=1
        p = input("¿Tu número es "+str(n)+"?, pon sí(sï es igual), o menor(sí tu número es menor): ")
    elif p =="mayor":
        n+=1
        p = input("¿Tu número es "+str(n)+"?, pon sí(sï es igual) o mayor(sí tu número es mayor): ")
print("Tu número es "+str(n))