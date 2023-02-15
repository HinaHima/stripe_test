"""URLs of the payment system itself"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name= 'main_page'),
    path('buy/<id>/', views.buy, name= 'buy'),
    path('item/<id>/', views.item, name='item')
]