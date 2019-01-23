from django.urls import path
from .views import func_gerenciar, func_create, func_delete, func_update, func_view

urlpatterns = [
               path('', func_gerenciar, name='func_gerenciar'),
               path('func_create', func_create, name='func_create'),
               path('func_delete', func_delete, name='func_delete'),
               path('func_update/<int:id>', func_update, name='func_update'),
               path('func_view/<int:id>', func_view, name='func_view'),
]
