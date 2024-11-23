# pr10_GomezGarcia_1184

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ") 
#Define una funcion que devuelve el número más grande de la lista
def max_in_list(lista):
    return max(lista)

# Invoca la funcion
print(max_in_list([3, 5, 7, 2])) 

![image](https://github.com/user-attachments/assets/6ef6f121-1483-435e-b0cf-c8571fd3c563)

![image](https://github.com/user-attachments/assets/7caf6919-cfb2-4a62-a32b-3fa7ac3744e6)


print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que devuelve la palabra más larga de la lista
def mas_larga(lista_palabras):
    return max(lista_palabras, key=len)

# Invoca la funcion
print(mas_larga(["gato", "elefante", "perro"]))  

![image](https://github.com/user-attachments/assets/d261e4db-6bc9-4f74-a85f-c64b66c7bdde)

![image](https://github.com/user-attachments/assets/cce5a181-7194-44f7-9e09-44bc3997ed58)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que devuelve las palabras con más de n caracteres
def filtrar_palabras(lista_palabras, n):
    return [palabra for palabra in lista_palabras if len(palabra) > n]

# Invoca la funcion
print(filtrar_palabras(["gato", "elefante", "perro"], 4)) 

![image](https://github.com/user-attachments/assets/b3a10c65-2268-4d30-8ec3-81ec10e98555)

![image](https://github.com/user-attachments/assets/54a23c1f-82b1-4e66-95f4-ec243e430515)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que cuenta las letras mayúsculas en la cadena
def contar_mayusculas(cadena):
    return sum(1 for char in cadena if char.isupper())

# Invoca la funcion
print(contar_mayusculas("Hola Mundo"))  

![image](https://github.com/user-attachments/assets/c9f85822-d943-4cf5-b85a-b08194c9621a)

![image](https://github.com/user-attachments/assets/e3dfb0a8-bd50-40d9-9d58-e3594f6a285d)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
# Define una funcion que convierte un número binario a entero
def binario_a_entero(binario):
    return int(binario, 2)

# Invoca la funcion
print(binario_a_entero("1010"))  

![image](https://github.com/user-attachments/assets/4d7575b3-475e-4611-9d91-219251da783d)

![image](https://github.com/user-attachments/assets/22107ee8-bf62-4ee2-94ea-21923ddf275c)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que devuelve la edad calculada a partir del año actual y el de nacimiento
def calcular_edad(actual, nacimiento):
    return actual - nacimiento

# Invoca la funcion
año_actual = 2024
personas = [("Juan", 2000), ("Ana", 1990), ("Pedro", 1985)]
for nombre, nacimiento in personas:
    print(f"{nombre} cumplirá {calcular_edad(año_actual, nacimiento)} años.")

![image](https://github.com/user-attachments/assets/de81a922-357d-4e82-859a-d85e4d7d6423)

![image](https://github.com/user-attachments/assets/2550ada7-7d5e-4b80-93a5-c529045b0b19)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que cuenta cuántas personas tienen más de 20 años
def contar_mayores_20(edades):
    return sum(1 for edad in edades if edad > 20)

# Invoca la funcion
print(contar_mayores_20([15, 25, 30, 18, 22])) 

![image](https://github.com/user-attachments/assets/516ed320-4877-4e51-b9a0-f49fb1c557d1)

![image](https://github.com/user-attachments/assets/b2b267fd-28f2-410b-aa80-dd488a306783)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que cuenta cuántos nombres empiezan con la letra indicada
def contar_nombres_con_letra(nombres, letra):
    return sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))

# Invoca la funcion
print(contar_nombres_con_letra(["Ana", "Juan", "Pedro", "Alma"], "a"))  

![image](https://github.com/user-attachments/assets/7b39a298-92a8-47f0-a4f3-892fd9705837)

![image](https://github.com/user-attachments/assets/77365784-b6f8-40ec-9cc6-d60c5bc0bd81)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que cuenta cuántas veces aparece cada vocal en la palabra
def contar_vocales(palabra):
    vocales = "aeiou"
    return {v: palabra.lower().count(v) for v in vocales}

# Invoca la funcion
print(contar_vocales("banana")) 

![image](https://github.com/user-attachments/assets/8f6b94ae-302f-41fb-9f88-4d309ee473db)

![image](https://github.com/user-attachments/assets/cd0a8838-1738-4cbd-b1bd-c8c741a3d8df)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que devuelve True si el año es bisiesto
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Invoca la funcion
print(es_bisiesto(2024)) 

![image](https://github.com/user-attachments/assets/116892dd-5595-4a3e-9f62-ae873bdf5114)

![image](https://github.com/user-attachments/assets/2f186c48-ff56-4853-8a49-b31d9a9e172a)



















