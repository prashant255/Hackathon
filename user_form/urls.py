from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.FirstPage.as_view(), name='First Page'),
    path('ajax/load-skills/', views.load_skills, name='ajax_load_skills'),
]
