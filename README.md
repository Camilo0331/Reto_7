# Reto_7
Aquí podran encontrar todos los puntos del reto 7

## Punto 1
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

### Código

Para esté punto utilice el while para repetir el proceso hasta 100, después de 100 dejara de hacerlo y así hacer una lista de todos, que mostrara los números del 1 al 100 y sus respectivos cuadrados.

```
i : int = 1
while i <= 100:
    print("El número "+ str(i)+" su cuadrado es: "+ str(i**2))
    i +=1
```

Para el diagrama utilice mermaid, el código lo pondre y adjuntare la imagen de mi diagrama.

![mermaid-diagram-2023-03-27-193802](https://user-images.githubusercontent.com/124615019/228097245-6b2d8542-63fa-4060-9ff1-b16894786472.png)

```
flowchart TD
    A[inicio] -->|i = 1| B{Mientras i <=100}
    B -->|No| D[fin]
    B -->|Sí| C(elevar al cuadrado a i)
    C --> E(Poner i y el resultado al elevarlo al cuadrado)
    E --> F(i = i +1)
    F --> B
```

## Punto 2

Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

Para este utilice por separado las funciones, relice 2 procesos para el primero defini los impares, n % 2, sí el resultado era distinto a 0 era impar. Para saber si era par hacia el mismo proceso pero si era igual a 0, se imprime el número par.

### Código
```
n : int = 1
print("Lista números impares")
while n <= 999 :   
     if n % 2 != 0:
          print(n)
     n +=1    

if __name__ == "__main__" :
     p : int = 2
     print("Lista de números pares")
     while p <= 1000:
          if p % 2 == 0:
               print(p)
          p+= 1 
 ```
 
 Para el diagrama utilice mermaid y explique el punto como lo pense.
 
 ![mermaid-diagram-2023-03-27-194848](https://user-images.githubusercontent.com/124615019/228098323-4943e072-7719-47c1-9346-bbae0cc4e3d7.png)
 
 ```
 flowchart TD
    A[inicio] -->|i = 1| b{mientras i sea menor o igual a 1000}
    b -->|Sí| c{i modulado 2 es igual a 0?}
    b -->|No| d[fin]
    c --> |Sí| e(i esta en los números pares)
    e --> |Lista de números primos| o(Imprimir i en la lista de los números pares)
    o --> p(i = i + 1)
    p --> b
    c --> |No| z{i modulado 2 es distinto a 0}
    z --> |Sí| x(i esta en los números impares)
    x --> |Lista de impares| y(Imprimir i en la lista de los impares)
    y --> p
    z --> |No| d
 ```
 
 ## Punto 3
 
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

El número dado con las condiciones dadas, hace un bucle toma el numero y va restando de a 1, va imprimiendo los números pares descendentes.

### Código

```
i : int
i = int(input("Ingrese un número mayor o igual a 2: "))
print("Lista descendente desde "+str(i)+" hasta 2")
while i >= 2:
    if i % 2 == 0:
        print(i)
    i -=1
```

Para el diagrama utilice mermaid y explico con secuencia lo que realice en el código

![mermaid-diagram-2023-03-27-195338](https://user-images.githubusercontent.com/124615019/228098844-b0984e9a-f548-4faf-8059-141d22f9a852.png)

```
flowchart TD
    A[inicio] -->|i = el número dado| b{mientras mayor o igual a 2}
    b -->|Sí| c{i modulado 2 es igual a 0?}
    b -->|No| d[fin]
    c --> e(imprimir i)
    e --> f(i = i - 1)
    f --> b
```

## Punto 4

En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18:9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

Para este cree la condición del bucle que el país A debe ser mayor a la población del país B, cuando se rompa el bucle al final sera dara el año del cual supera esa condición y el bucle acaba.

### Código

```
A : float = 25000000
B : float = 18900000
año : float = 2022
while A>=B :
    A = A + (A*(2/100))
    B = B + (B*(3/100))
    año +=1
print(año)
```

## Punto 5

Imprimir el factorial de un número natural n dado.

Para este punto se investiga y se haya que es multiplicar el número dado con lo anteriores naturales, para este se hace un bucle que multipleque el número y vaya descendiendo una unidad y asi hasta que llegue a 0, se rompa el bucle y nos de el resultado.

### Código

```
i : int = 1
n : int
n = int(input("Ingrese el número natural: "))
while n > 0:
    i = i *n
    n -=1
print ("El factorial del número ingresado es: "+str(i))
```

## Punto 6

Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.

Para este vamos descartando la mitad para saber si tú número es menor o mayor a 50, va preguntado sucesivamente hasta que llega a la respuesta.

### Código

```
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
```

## Punto 7

Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

Para este punto pose varias condiciones, le puse el rango que debia tener y que cumpliera de que "f" o sea el divisor fuera aumentado y rompiera el bucle cuando llegara al mismo número ingresado, el bucle consistia en probar uno por uno los divisores hasta llegar al número dado y si cumplian con la condición de residuo 0, eran divisores

### Código

```
f : int = 1
n : int
n = int(input("Ingrese un número del 2 al 50 para hallar sus divisores: "))
while n >= 2 and n <= 50 and f <= n : 
    if n % f == 0:
        print(str(f)+" es un número divisor de "+str(n))
    f+=1
```

## Punto 8

Implementar el algoritmo que muestre los números primos del 1 al 100. nota: use funciones

Para este primero diseñe la función para que nos diera los números primos, los cuales solo son divisibles por uno y por ellos mismo así con esto pude realizar, para este utilice if__name__=="__main__", después traje la función previamente realizada y imprimí los números que era primos del 1 al 100, que son 25.

### Código

```
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
```

### ¡Muchas gracias por dedicarle el tiempo al repo, no olvides dejar tu estrellita!
