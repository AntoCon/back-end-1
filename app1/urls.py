from django.urls import path
from . import views #importo vistas del app1, traigo el archivo para usar su info


urlpatterns = [
    path('inicio/', views.index), #dejo el mapeo paraq en el navegador se muestre el inicio en la ruta
    path('inicio2/', views.funcion),
]
