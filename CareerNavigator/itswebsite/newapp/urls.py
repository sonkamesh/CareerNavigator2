from django.urls import path
from . import views

urlpatterns = [
    path('', views.newapp_home, name='newapp_home'),
    path('<int:pk>', views.NewappDetailView.as_view(), name='newapp-detail'),
]
