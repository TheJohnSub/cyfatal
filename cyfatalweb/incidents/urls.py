from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:incident_id>/', views.detail, name='detail'),
	path('about/', views.about_page_view, name='about'),
	path('contact/', views.contact_page_view, name='contact')

]