from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .forms import EntrarForm

urlpatterns = [
    path(
        "entrar/",
        LoginView.as_view(
            template_name="contas/entrar.html",
            authentication_form=EntrarForm,
            redirect_authenticated_user=True,
        ),
        name="entrar",
    ),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("sair/", LogoutView.as_view(), name="sair"),
]
