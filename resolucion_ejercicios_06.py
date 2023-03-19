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
    def get_name(self):
        return self.__nombre

    @get_name.setter
    def set_name(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def get_age(self):
        return self.__edad

    @get_age.setter
    def set_age(self, edad_nueva):
        self.__nombre = edad_nueva

    @property
    def get_dni(self):
        return self.__dni

    @get_dni.setter
    def set_dni(self, dni_nuevo):
        self.__nombre = dni_nuevo

    def mostrar(self):
        return f"El nombre de la persona es: {self.get_name}, edad: {self.get_age} años y dni: {self.get_dni}"

    def es_mayor_de_edad(self):
        if self.__edad >= 18:
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