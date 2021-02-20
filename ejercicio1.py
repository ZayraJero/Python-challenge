def number_lenght(number_param):
    if not isinstance(number_param, int): #Validamos que no sea negativo pero si entero
        return None, "Tiene que ser un núnmero"
    elif number_param < 0: 
        return None, "No usar números negativos" #Para ser doble comprobación
        num_str = str(number_param) 
        count = 0 #Contador que se va incrementando en cada iteración
    for element in num_str:
        count += 1; #Se va iterando 1 por 1 
    return count

number_lenght(459687)
number_lenght(True)
