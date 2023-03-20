"""Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
1- Un constructor.
2- Los setters y getters para el nuevo atributo.
3- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
4- Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
5- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta."""
from resolucion_ejercicios_07 import Cuenta

class Cuenta_Joven(Cuenta):

    def __init__(self, nombre = None, edad = None, dni = None, cantidad= None, bonificacion = None):
        super().__init__(nombre, edad, dni, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def es_titulatar_valido(self):
        if self.age > 17 and self.age < 26:
            return True
        return False

    def retirar(self, cantidad):
        try:
            if self.es_titulatar_valido() == True:
                saldo = self.cantidad - cantidad
                self.cantidad = saldo
                print(f"Se retira {cantidad} de la cuenta, su nuevo saldo es: {round(saldo,2)}")
            else:
                print("El titular no es válido")
        except TypeError:
            print("Ingrese un monto válido.")

    def mostrar(self):
            if self.age > 17 and self.age < 26:
                print(f"Es una cuenta joven y la bonificacion es: {self.bonificacion}%")
            else:
                print(f"El nombre de la persona es: {self.name}, edad: {self.age} años y dni: {self.dni}. Su saldo en la cuenta es: {self.cantidad}")


if __name__ == "__main__":
    cuenta_joven_1 = Cuenta_Joven("Juan", 20, 123456789, 500.20, 20.6)
    cuenta_joven_1.mostrar()
    cuenta_joven_1.retirar(200)
    cuenta_joven_1.retirar(35.35)
    cuenta_joven_1.retirar("hola")
    print(cuenta_joven_1.es_titulatar_valido())

    cuenta_adulta_1 = Cuenta_Joven("Juan", 34, 123456789, 500.20, 20.6)
    cuenta_adulta_1.mostrar()
    cuenta_adulta_1.retirar(200)
    print(cuenta_adulta_1.es_titulatar_valido())