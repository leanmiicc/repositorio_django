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
from resolucion_ejercicios_06 import Persona

class Cuenta(Persona):

    def __init__(self, nombre = None, edad = None, dni = None, cantidad= None):
        super().__init__(nombre, edad, dni)
        self.__cantidad = cantidad

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad_new):
        self.__cantidad = cantidad_new

    def mostrar(self):
        print(f"El nombre de la persona es: {self.name}, edad: {self.age} años y dni: {self.dni}. Su saldo en la cuenta es: {self.cantidad}")

    def ingresar(self, cantidad):
        try:
            if cantidad < 0:
                print("No se puede ingresar una cantidad negativa")
            else:
                saldo = self.cantidad + cantidad
                self.cantidad = saldo
                print(f"Se ingresa {cantidad} a la cuenta, su nuevo saldo es: {round(saldo,2)}")
        except TypeError:
            print("Ingrese un monto válido.")


    def retirar(self, cantidad):
        try:
            saldo = self.cantidad - cantidad
            self.cantidad = saldo
            print(f"Se retira {cantidad} de la cuenta, su nuevo saldo es: {round(saldo,2)}")
        except TypeError:
            print("Ingrese un monto válido.")

if __name__ == "__main__":
    cuenta_1 = Cuenta("Juan", 25, 123456789, 500.20)
    cuenta_1.mostrar()
    cuenta_1.ingresar(100)
    cuenta_1.ingresar(100)
    cuenta_1.ingresar("hola")
    cuenta_1.retirar(100)
    cuenta_1.retirar(300)
    cuenta_1.retirar(150.75)
    cuenta_1.retirar("hola")
