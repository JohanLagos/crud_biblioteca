from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path("logout", views.logout_request, name= "logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)