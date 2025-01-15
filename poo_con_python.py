class Personaje:
    '''
    # Atributos de la clase
    nombre = ""
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    '''
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        print(self.__nombre)
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Defensa:", self.__defensa)
        print("-vida:", self.__vida)
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia += inteligencia
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa += defensa
        self.__defensa = self.__defensa + defensa
    def esta_vivo(self):
        return self.__vida > 0
    def morir(self):
        self.__vida = 0
        print(self.__nombre, "se murióooo")
    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa if self.__fuerza > enemigo.__defensa else 0
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "Ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if not enemigo.esta_vivo():
            enemigo.morir()
        print("Vida de ", enemigo.__nombre, " es", enemigo.__vida)

# Creando clase "G" que hereda de su clase padre "Personaje"
class Guerrero(Personaje):
    # Sobreescribir el contructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
    # Llamar a la clase padre    
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

hercules = Guerrero("Hércules", 80, 80, 100, 100)
hercules.atributos()

'''
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
       if fuerza < 0:
          print("Error")
       else:
        self.__fuerza = fuerza
'''   
# Variable del constructor vacío de la clase
mi_personaje = Personaje("Trakalosa de monterrey", 100, 90, 50, 100)
mi_enemigo = Personaje("La arrolladora", 60, 90, 0, 100)

#print(mi_personaje.morir())
#print(mi_personaje.esta_vivo())
#+print (mi_personaje.dañar(mi_enemigo))
#mi_personaje.atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()

#Prueba 1. Sin acceso al atributo fuerza
'''
mi_personaje.__Personaje__fuerza = 10
mi_personaje.atributos()
'''
