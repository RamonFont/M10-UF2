import random

num = 0
endivinar = random.randint(1, 100)

while int(num) != endivinar:
    num= input("Escriu un num")
    if(int(num) == endivinar):
        print("Molt bé")
    elif(int(num) > endivinar):
        print("El número secret es més petit")
    else:
        print("El número secret és més gran")
