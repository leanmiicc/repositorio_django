from resolucion_ejercicios_06 import Persona

"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
1- Un constructor, donde los datos pueden estar vacíos.
2- Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
3- mostrar(): Muestra los datos de la cuenta.
4- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
5- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos."""

class Cuenta(Persona):

    def __init__(self, nombre = None, edad = None, dni = None, cantidad= None):
        super().__init__(nombre, edad, dni)
        self.__cantidad = cantidad

    @property
    def get_cantidad(self):
        return self.__cantidad

    @get_cantidad.setter
    def set_prueba(self, cantidad_new):
        self.__cantidad = cantidad_new

    def mostrar(self):
        print(f"El nombre de la persona es: {self.get_name}, edad: {self.get_age} años y dni: {self.get_dni}. Su saldo en la cuenta es: {self.get_cantidad}")

    def ingresar(self, cantidad):
        if cantidad < 0:
            print("No se puede ingresar una cantidad negativa")
        else:
            saldo = self.get_cantidad + cantidad
            print("Su nuevo saldo es: ", saldo)

    def retirar(self, cantidad):
        saldo = self.get_cantidad - cantidad
        print(f"Se retira {cantidad} a la cuenta")
        print(f"Su nuevo saldo es: {saldo}")

if __name__ == "__main__":
    cuenta_1 = Cuenta("Juan", 25, 123456789, 500.20)
    cuenta_1.mostrar()
    cuenta_1.ingresar(100)
    cuenta_1.retirar(100)




