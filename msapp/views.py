from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Modelo1
from .forms import Modelo1Form


# Create your views here.
def index(request):
	titulo 	= 'Index'
	template = loader.get_template('msapp/index.html')
	
	context = {
		'titulo': titulo,
	}

	return HttpResponse(template.render(context, request))


@login_required
def modelo1_nuevo(request):
	titulo 	= 'Producto nuevo'
	template = loader.get_template('msapp/modelo1/new.html')

	modelo_context = Modelo1Form(prefix='modelo1')

	if request.method == 'POST':
		modelo 	= Modelo1Form(request.POST, prefix='modelo1')


		if modelo.is_valid():

			modelo = modelo.save(commit=False)
			modelo.usuario = request.user
			modelo.save()
			messages.success(request, 'Éxito. Se ha creado correctamente.')
			return redirect('modelo1_index')
		else:
			modelo_context 	= modelo

	context = {
		'titulo'	: titulo,
		'modelo'	: modelo_context
 	}

	return HttpResponse(template.render(context, request))


@login_required
def modelo1_index(request):
	titulo 	= 'Index'
	template = loader.get_template('msapp/modelo1/index.html')

	usuario_logueado = request.user
	modelo_context = Modelo1.objects.filter(usuario=usuario_logueado)


	context = {
		'titulo'	: titulo,
		'productos' 	: modelo_context,
	}

	return HttpResponse(template.render(context, request))


from django.core.exceptions import ObjectDoesNotExist


@login_required
def modelo1_show(request, id):
	titulo 	= 'Ver'
	template = loader.get_template('msapp/modelo1/show.html')

	usuario_logueado = request.user

	try:
		modelo 	= Modelo1.objects.get(usuario=usuario_logueado, pk=id)
		context = {
			'titulo'	: titulo,
			'modelo'	: modelo,
		}
	except ObjectDoesNotExist:
		messages.error(request, 'Error. No existe dicho producto')
		return redirect('modelo1_index')

	return HttpResponse(template.render(context, request))


@login_required
def modelo1_edit(request, id):
	titulo 	= 'Editar Producto'
	template = loader.get_template('msapp/modelo1/new.html')

	usuario_logueado = request.user

	try:
		producto_edit 	= Modelo1.objects.get(usuario=usuario_logueado, pk=id)
	except ObjectDoesNotExist:
		messages.error(request, 'Error. No existe dicho producto')
		return redirect('modelo1_index')

	modelo_context = Modelo1Form(prefix='modelo1_edit', instance=producto_edit)

	if request.method == 'POST':
		modelo 	= Modelo1Form(request.POST, prefix='modelo1_edit')


		if modelo.is_valid():
			modelo = modelo.save(commit=False)
			modelo.usuario = request.user
			modelo.save()
			return redirect('modelo1_index')
		else:
			modelo_context 	= modelo
			print('hello')

	context = {
		'titulo'	: titulo,
		'modelo'	: modelo_context
 	}

	return HttpResponse(template.render(context, request))



##plot grafico
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

def getimage(request):

	x = np.arange(8)
	s = np.piecewise(x, [x < 3, x >= 4], [lambda x: -x, lambda x: 2 * x])
	plt.plot(x, s)
	 
	plt.xlabel('Dias')
	plt.ylabel('Inventario Actual')
	plt.title('Inventario')
	plt.grid(True)
 	
	response = HttpResponse(content_type="image/jpeg")

	plt.savefig(response, format="jpg")
	return response