from django.urls import path, include
from loteria.views import dashboard, apostasLoteria, aut_user, home, logout_user

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('loteria/<int:id>/', apostasLoteria, name='loteria'),
    path('login/', aut_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
