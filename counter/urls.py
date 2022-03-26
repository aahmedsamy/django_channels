from django.urls import path

from counter.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]