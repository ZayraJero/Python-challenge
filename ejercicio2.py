def list_of_multiples(num, len):
    list_new = [] #Donde se agregaran la lista
    multiple = num
    a = isinstance(num, int) #Validar que sea entero
    b = isinstance(len , int)
    if a != True or b != True: #Si son diferentes a true estan mal
        return None, "Tiene que ser un núnmero"
    elif num < 0 or len < 0 :
        return None, "Tiene que ser número positivo"
    for item in range(len):
        multiple += num * item 
        list_new.append(multiple) #Agregando a la lista
    return list_new

list_of_multiples(5, 10)