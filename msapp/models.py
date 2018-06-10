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
	#stock 		= models.IntegerField(verbose_name = "Stock actual", default=100)
	
	#Tiempo de simulacion
	tiempo 	= models.FloatField(default=1)

	#Tasa de demanda (unidades por unidad de tiempo)
	d		= models.IntegerField(verbose_name='Tasa de Demanda')

	#Costo de preparación correspondiente 
	#a la colocación de un pedido ($/pedido)		
	k 		= models.FloatField(verbose_name='Costo de Preparación de Pedido')		

	#Costo de almacenamiento 
	#($ por unidad en inventario por unidad de tiempo)
	h 		= models.FloatField(verbose_name='Costo de Almacenamiento')

			
	
	def __str__(self):
		return self.nombre

	def inventario_promedio(self):
		return self.d / 2
	ip = property(inventario_promedio)

	def lote_optimo_compra(self):
		return round(sqrt((2*self.k*self.d)/self.h))
	y = property(lote_optimo_compra)

	def longitud_ciclo(self):
		return round(self.y / (self.d/self.tiempo) )
	lc 	= property(longitud_ciclo)

	def costo_inventario(self):
		return round(self.k/(self.y/self.d) + self.h*(self.y/2))
	ci = property(costo_inventario)