# kodemia-retos-python-20-02-21

Retos sabatinos

### Code styling

- TODAS las variables y funciones son `snake_case`
- TODAS las clases son `camelCase`
- TODO el código va comentado
- El nombre de las variables, funciones, clases tiene que ser legible

## Ejercicio 1

Crear una funcion que reciba un numero como argumento y devuelva el largo de este numero

**Ejemplo**

`number_length(10) -> 2`

`number_length(10000) -> 5`

`number_length(4321) -> 4`

**Restricciones**

- El numero no puede ser negativo
- El numero que se MANDA a la funcion tiene que ser de tipo INT
- **NO** se puede utilizar el metodo length

**Tips**

- Los numeros en python carecen de indexación :poop:
- Los strings son iterables (estan indexados -> osea tienen indices) :white_check_mark:

## Ejercicio 2

Crear una funcion que reciba dos numeros como argumentos (numero, longitud), y devolver una lista con los multiplos del numero dada la longitud

**Ejemplos**

`list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]`

`list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]`

**Notas**

Vean que la lista contiene el numero que le pasan como argumento

**Restricciones**

- Los argumentos no puede ser negativos
- Los argumentos deben ser enteros

**Tips**

- Cómo saco un rango de un numero? `3 -> [1,2,3]`

## Ejercicio 3

Crear una funcion que devuelva el factorial de un numero

**Ejemplos**

`factorial(3) -> 6` (3*2*1)

`factorial(4) -> 24` (4*3*2\*1)

**Tips**

- Investigar que demonios es recursividad

## Ejercicio 4

Crear una funcion que formatee numeros :smile:

**Ejemplos**

`format_numer(1000) -> '1,000'`

`format_numer(43214124) -> '43,214,124'`

**Restricciones**

- El argumento no puede ser negativo
- El argumento deben ser entero

### Ejercicio 4.1

- Agregar el separador que el usuario indique

**Ejemplo**

`format_numer(1000,'#') -> '1#000'`

`format_numer(43214124) -> '43#214#124'`
