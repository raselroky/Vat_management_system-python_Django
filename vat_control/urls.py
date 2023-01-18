from django.urls import path
from . import views

urlpatterns = [
    path('vat/',views.VATView.as_view()),
]