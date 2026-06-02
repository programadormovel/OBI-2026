# criação de variável 
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

if numero1 < numero2 and numero1 < numero3:
    print(numero1)
elif numero2 < numero1 and numero2 < numero3:
    print(numero2)        
else:
    print(numero3)

if numero1 > numero2 and numero1 < numero3 or numero1 < numero2 and numero1 > numero3:
    print(numero1) 
elif numero2 > numero1 and numero2 < numero3 or numero2 < numero1 and numero2 > numero3:
    print(numero2)  
else:    
    print(numero3)
    
if numero1 > numero2 and numero1 > numero3:
    print(numero1)        
elif numero2 > numero1 and numero2 > numero3:
    print(numero2)        
else:    
    print(numero3)   


        