from django.shortcuts import render

from django.contrib import admin
from django.urls import path , include


from .views import      CreadorListView   \
                    ,   CreadorDetailView \
                    ,   CreadorCreateView \
                    ,   CreadorUpdateView \
                    ,   CreadorDeleteView

app_name = "creador"

urlpatterns = [
    path("", CreadorListView.as_view(), name="all"),
    path("create/", CreadorCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", CreadorDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CreadorUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CreadorDeleteView.as_view(), name="delete")

]