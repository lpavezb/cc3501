# -*- coding: iso-8859-1 -*-

#####################################################################
# Daniel Calderon S.
# CC3501 - otoño 2011
#####################################################################

# Vector2D.py
# versión 20111_2d01
# ---------------
# Operaciones básicas para manejar vectores en 2 dimensiones.
# ---------------
# contenido:

## Clase Vector
### Vector -> constructor cartesiano
### x,y -> componentes cartesianas
### setX,setY -> sin retorno, asigna x e y
### angulo -> componente angular en radianes (coord. polares)
### anguloG -> componente angular en grados (coord. polares)
### modulo -> módulo del vector
### norma2 -> modulo o norma al cuadrado
### polares -> [modulo, ángulo] (coord. polares)
### cartesianas -> [x,y] (coord. cartesianas)
### clon -> copia del vector actual

## Funciones para clase Vector
### VectorPolar -> "constructor" polar
### sumar -> suma de dos vectores
### restar -> resta de dos vectores
### ponderar -> ponderación del vector por el escalar indicado
### normalizar -> vector normalizado
### angulo -> ángulo entre dos vectores
### rotar -> vector rotado en el ángulo indicado en radianes
### distancia -> distancia entre ambos vectores
### punto -> producto punto entre dos vectores

#* Observación:
## método o función -> variable de retorno

# Implementación testeada con:
## Python 2.6

#####################################################################

import math as mt

#####################################################################

class Vector:
	def __init__(self, x, y):
		self.a = [0,0]
		self.a[0] = x
		self.a[1] = y
	
	def x(self):
		return self.a[0]
	
	def y(self):
		return self.a[1]
	
	def setX(self,x):
		self.a[0] = x
	
	def setY(self,y):
		self.a[1] = y

	def angulo(self):
		if self.x!=0:
			return mt.atan2(self.y(),self.x())
		else:
			if self.y>0:
				return mt.pi/2.0
			else:
				return -mt.pi/2.0

	def anguloG(self):
		return self.angulo()*180.0/mt.pi

	def modulo(self):
		return (self.x()**2 + self.y()**2)**0.5
		
	def norma2(self):
		return (self.x()**2 + self.y()**2)

	def polares(self):
		return self.modulo(),self.angulo()

	def cartesianas(self):
		return self.a
	
	def clon(self):
		return Vector(self.x(),self.y())

#####################################################################

def VectorPolar(m,a):
	return Vector(m*mt.cos(a),m*mt.sin(a))

def sumar(r1,r2):
	return Vector(r1.x() + r2.x(), r1.y() + r2.y())

def restar(r1,r2):
	return Vector(r1.x() - r2.x() , r1.y() - r2.y())

def ponderar(a,r):
	return Vector(a*r.x(),a*r.y())

def normalizar(r):
	m=r.modulo()
	if m>0:
		return Vector(r.x()/m,r.y()/m)
	else:
		return r

def angulo(r1,r2):
	return r1.angulo()-r2.angulo()

def rotar(r,a):
	return VectorPolar(r.modulo(),r.angulo()+a)

def distancia(r1,r2):
	return restar(r1,r2).modulo()

def punto(r1,r2):
	return r1.x()*r2.x()+r1.y()*r2.y()
	
def cruz(u,v):
	return [0,0,u.x()*v.y() - u.y()*v.x()]

#####################################################################