from django.contrib import admin
from django.urls import path
from academico import views
urlpatterns = [path('admin/',admin.site.urls),path('',views.inicio,name='inicio'),path('<str:modulo>/',views.listado,name='listado'),path('<str:modulo>/nuevo/',views.editar,name='crear'),path('<str:modulo>/<int:pk>/editar/',views.editar,name='editar'),path('<str:modulo>/<int:pk>/eliminar/',views.eliminar,name='eliminar')]
