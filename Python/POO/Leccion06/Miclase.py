class Miclase:

    #variable de clase: se asocia con la clase en si misma no con los objetos
    variable_clase ='---Valor variable clase'
    #variable de instancia
    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia
# metodos estaticos  es decir de la clase, estas no pueden acceder a las variable s de instancia
    @staticmethod
    def metodo_estatico():
        #el self no se puede usar en este metodo
        #se puede acceder a la variable de clase
        print(Miclase.variable_clase)

    #metodo de clase y si recibe variables
    #similar al self
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    #metodo de instancia se peuden acceder tanto al metodo de clase como el estarico
    def metodointancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_instancia)
        print(self.variable_clase)
#para acceder a variable de clase no es necesario crear un objeto
print(Miclase.variable_clase)
# para acceder a la varialbe de instancia se cra el objeto
Miclase1 = Miclase('valor variable instancia')

print(Miclase1.variable_instancia)
print(Miclase1.variable_clase)

Miclase.variable_clase2 = 'valor variable clase 2'

miclase2 = Miclase('otro valor de instancia')
print(miclase2.variable_instancia)
print(miclase2.variable_clase)
print(miclase2.variable_clase2)


#llamado al metodo estatico
Miclase.metodo_estatico()
#llamado al metodo de clase

Miclase.metodo_clase()
miobjeto1 = Miclase('variable de instancia')
miobjeto1.metodo_clase()
miobjeto1.metodointancia()
