"""Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
1- Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
2- mostrar(): Muestra los datos de la persona.
3- Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad."""

class Persona():
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def name(self):
        return self.__nombre

    @name.setter
    def name(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def age(self):
        return self.__edad

    @age.setter
    def age(self, edad_nueva):
        self.__nombre = edad_nueva

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni_nuevo):
        self.__nombre = dni_nuevo

    def mostrar(self):
        return f"El nombre de la persona es: {self.name}, edad: {self.age} años y dni: {self.dni}"

    def es_mayor_de_edad(self):
        if self.age >= 18:
            return True
        return False

if __name__ == "__main__":

    persona_uno = Persona("Juan", 25, 123456789)
    print("datos persona_uno -->", persona_uno.mostrar())
    print(persona_uno.es_mayor_de_edad())

    persona_dos = Persona("Lucia", 14, 123456789)
    print("datos persona_dos -->", persona_dos.mostrar())
    print(persona_dos.es_mayor_de_edad())

    persona_tres = Persona("Hernan", 18, 123456789)
    print("datos persona_tres -->", persona_tres.mostrar())
    print(persona_tres.es_mayor_de_edad())

    persona_cuatro = Persona("Leticia", 15, 123456789)
    print("datos persona_cuatro -->", persona_cuatro.mostrar())
    print(persona_cuatro.es_mayor_de_edad())