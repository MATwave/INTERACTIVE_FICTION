from django.urls import path

from .views import BookView
from .views import IndexView
from .views import PageView
from .views import RegistrationView
from .views import TakeView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path("book/<int:book_id>", BookView.as_view(), name="book"),
    path("book/<int:book_id>/page/<int:page_id>", PageView.as_view(), name="page"),
    path("book/<int:book_id>/page/<int:page_id>/take/<int:item_id>", TakeView.as_view(), name="take"),
]
