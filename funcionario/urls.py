from django.urls import path
from .views import func_gerenciar, \
                    func_create, \
                    func_delete, \
                    func_update, \
                    func_view, \
                    setor_gerenciar, \
                    setor_create, \
                    setor_delete, \
                    setor_update, \
                    setor_view

urlpatterns = [
    path('', func_gerenciar, name='func_gerenciar'),
    path('func_create', func_create, name='func_create'),
    path('func_delete/<int:id>', func_delete, name='func_delete'),
    path('func_update/<int:id>', func_update, name='func_update'),
    path('func_view/<int:id>', func_view, name='func_view'),
    path('setor_create', setor_create, name='setor_create'),
    path('setor_delete/<int:id>', setor_delete, name='setor_delete'),
    path('setor_update/<int:id>', setor_update, name='setor_update'),
    path('setor_view/<int:id>', setor_view, name='setor_view'),
    path('setor_gerenciar', setor_gerenciar, name='setor_gerenciar'),

]
