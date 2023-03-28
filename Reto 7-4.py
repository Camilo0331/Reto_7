A : float = 25000000
B : float = 18900000
año : float = 2022
while A>=B :
    A = A + (A*(2/100))
    B = B + (B*(3/100))
    año +=1
print(año)