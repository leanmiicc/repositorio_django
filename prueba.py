class Persona():

    def __init__(self,nombre,apellido,dni,email):
        self.__nombre = nombre
        self._apellido = apellido
        self.dni = dni
        self.email = email

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


    #GETTER
    @property
    def pepe(self):
        return self.__nombre

    #SETTER
    @pepe.setter
    def pepe(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    def mostrar(self):
        return self.dni

    def mostrar(self):
        return f"El nombre de la persona es: {self.dni}, edad: {self.email}"



estudiante_uno = Persona('Jose','Argento',34111222,'pepe@gmail.com')
print(estudiante_uno.mostrar())
