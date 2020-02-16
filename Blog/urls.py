from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:post_uuid>/', views.detail, name='detail'),
    path('<uuid:post_uuid>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('<str:label>', views.search, name='search'),
]