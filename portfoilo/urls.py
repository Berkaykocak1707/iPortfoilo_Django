from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portfoilo-index'),
    path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
    path('send_email/', views.send_email, name='send_email'),
]