from django.urls import path
from .views import index, add, edit, delete

urlpatterns = [    
    path('', index, name='index'),
    path('/add', add, name='add'),
    path('/edit', edit, name='edit'),
    path('/delete', delete, name='delete')
]