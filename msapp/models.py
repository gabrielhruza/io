from django.db import models
from django.contrib.auth.models import User

from math import sqrt


# Create your models here.
class Usuario(models.Model):
    user 		= models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
    	return self.username


class Modelo1(models.Model):
	nombre_producto		= models.CharField(max_length=50)
	categoria	= models.CharField(max_length=50)
	usuario 	= models.ForeignKey(User, on_delete=models.CASCADE)

	#stock actual
	stock 		= models.IntegerField()

	#Cantidad pedida (cantidad de unidades)
	y 		= models.IntegerField()
	
	#Tiempo de simulacion
	tiempo 	= models.IntegerField()

	#Tasa de demanda (unidades por unidad de tiempo)
	d		= models.IntegerField()

	#Costo de preparación correspondiente 
	#a la colocación de un pedido ($/pedido)		
	k 		= models.IntegerField()		

	#Costo de almacenamiento 
	#($ por unidad en inventario por unidad de tiempo)
	h 		= models.IntegerField()		
	
	def __str__(self):
		return self.nombre

	def duracion_ciclo_pedido(self):
		return self.y / self.d
	t = property(duracion_ciclo_pedido)

	def inventario_promedio(self):
		return self.y / 2
	ip = property(inventario_promedio)

	def lote_optimo_compra(self):
		return sqrt((2*self.k*self.d)/self.h)
	loc = property(lote_optimo_compra)

	def longitud_ciclo(self):
		return self.loc / self.d
	lc 	= property(longitud_ciclo)