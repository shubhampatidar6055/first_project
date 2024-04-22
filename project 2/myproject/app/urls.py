from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("data/", table),
    path("registration/", create_user),
    path("delete/<int:pk>/", delete, name="delete"),
    path("update/<int:uid>/", update_user, name="update"),
    path("update_user/",update_data),
]
