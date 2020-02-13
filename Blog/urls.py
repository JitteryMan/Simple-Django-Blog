from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:post_uuid>', views.detail, name='detail'),
    path('django/', views.django, name='django'),
]