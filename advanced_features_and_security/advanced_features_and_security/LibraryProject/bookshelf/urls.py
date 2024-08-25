from django.urls import path
#from  . import apps
from . import views  # Assuming you have views.py with a view function

urlpatterns =[
    #path("",apps.BookshelfConfig, name="bookshelf")
    path("", views.index, name="bookshelf"),
]