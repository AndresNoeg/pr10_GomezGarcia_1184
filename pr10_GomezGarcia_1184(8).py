print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que cuenta cuántos nombres empiezan con la letra indicada
def contar_nombres_con_letra(nombres, letra):
    return sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))

# Invoca la funcion
print(contar_nombres_con_letra(["Ana", "Juan", "Pedro", "Alma"], "a"))  
