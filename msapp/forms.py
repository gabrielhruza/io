from django.forms import ModelForm
from .models import Modelo1

# Create the form class.
class Modelo1Form(ModelForm):
	class Meta:
		model 	= Modelo1
		fields 	= ['nombre_producto', 'categoria', 'stock', 'y', 'tiempo', 'd', 'k', 'h']