def number_lenght(number_param):
      if number_param > 0: #Validamos que no sea negativo
        num_str = str(number_param) 
        count = 0 #Contador que se va incrementando en cada iteración
        for element in num_str:
            count += 1; #Se va iterando 1 por 1 
        return count
      else:
        return None, "No usar números negativos" #Para ser doble comprobación

number_lenght(459687)