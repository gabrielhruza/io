from django.urls import path

from . import views

urlpatterns = [
    #path('articles/2003/', views.special_case_2003),
    #path('articles/<int:year>/', views.year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    path('', views.index, name='index'),
    path('modelo1/nuevo', views.modelo1_nuevo, name='modelo1_nuevo'),
    path('modelo1/index', views.modelo1_index, name='modelo1_index'),
    path('modelo1/show/<id>/', views.modelo1_show, name='modelo1_show'),
    path('modelo1/edit/<id>/', views.modelo1_edit, name='modelo1_edit'),
    path('plot', views.getimage, name='getimage'),
]