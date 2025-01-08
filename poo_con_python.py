class Personaje:
    # Atributos de la clase
    nombre = 'default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 15

# Variable del constructor vacío de la clase
mi_personaje = Personaje()

# Modficando los valores de los atributos
mi_personaje.nombre = "Noob"
mi_personaje.fuerza = 11

# Print 
print ("El nombre del personaje es", mi_personaje.nombre)
print ("La fuerza de mi personaje es", mi_personaje.fuerza)


