from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'producto', views.ProductoViewSet,basename='producto')

urlpatterns = [
    path('',views.CategoriaView.as_view()),
    path('categoria/<int:categoria_id>', views.CategoriaDetailView.as_view()),
    path('Produc',views.ProductoView.as_view()),
    path('adminRouter',include(router.urls))
]
