class Estudiante(object):
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad 
        
	def hola(self):
		return 'Mi nombre es is %s' % self.nombre
        
e = Estudiante("Arturo",22)
print e.hola()