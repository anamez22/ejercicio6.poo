def __init__(self, nombre, edad):
    self.__nom = nombre
    self.__edad = edad 

def get_nom(self):
    return self.__nom

def set_nom(self, nombre):
    self._nom = nombre

def get_edad(self):
    return self._edad

def set_edad(self, edad):
    if edad >=0:
        self.__edad = edad 
    else:
        print("La edad no puede ser negativa. ")

persona = Persona ("Maria", 19)

print(persona.get_nom())
print(persona.get_edad())

persona.set_nom("luis")
persona.set_edad(25)
persona.set_edad(-3)

print(persona.get_nom())
print(persona.get_edad())
