from django.urls import path

from .views import index_view
from .views import PageView


app_name = 'Pages'

urlpatterns = [
    path('', index_view, name='index'),
    path('<slug:title_slug>/', PageView.as_view(), name='target_page'),
]
