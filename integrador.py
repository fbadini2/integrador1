class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

class Cuenta(Persona):

    def __init__(self, nombre, edad, DNI=None, cantidad:float=0):
        super().__init__(nombre, edad, DNI)
        self.__titular = nombre
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular   
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print('\nTitular : {} \nCantidad: {}'.format(self.__titular, self.__cantidad))

    def ingresar(self, cantidad:float=0):
        try:
            cantidad = float(input("\nCantidad a ingresar?: "))
            if cantidad > 0:
                self.__cantidad = self.__cantidad + cantidad
        except:
            print("Debe introducir un número valido.")

    def retirar(self, cantidad:float=0):
        try:
            cantidad = float(input("\nCuanto desea retirar?: "))
            self.__cantidad = self.__cantidad - cantidad
        except:
            print("Debe introducir un número valido.")


class CuentaJoven(Cuenta):
    def __init___(self, titular, edad, cantidad, bonificacion):
         super().__init__(titular, edad, cantidad)
         self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonif:int=0):
        self.__bonificacion = bonif

    def es_titular_valido(self):
        if self.edad >= 18 and self.edad < 25:
            return True
        else:
            print('Titular no valido!!')
    
    def mostrar(self):
        super().mostrar()
        if self.es_titular_valido():
            print('CUENTA JOVEN (Bonificación : {}'.format(self.__bonificacion) + '%)')

    def retirar(self):
        if self.es_titular_valido():
            super().retirar()
        else:
            print('No puede retirar!!')




cuenta1 = Cuenta("Juan", 50)

cuenta2 = CuentaJoven("Pedro", 25)

cuenta2.bonificacion = 20

cuenta1.ingresar()

cuenta1.retirar()

cuenta2.ingresar()

cuenta2.retirar()

cuenta1.mostrar()

cuenta2.mostrar()
