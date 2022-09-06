from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),

    path('add/', views.create, name="create"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('update/<int:pk>', views.update, name="update"),
]