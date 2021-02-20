##Recursividad se hace llamar a si misma

def factorial(number): 
    if number > 1: #Cuando este en uno se detendra
        return number * factorial(number - 1) #Se multiplica el numero por el resultado del otro 
    else:
        return 1

factorial(4)