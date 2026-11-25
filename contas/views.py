from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import CadastroForm


def _destino_seguro(request, destino):
    """Só aceita redirecionar para endereços do próprio site."""
    ok = url_has_allowed_host_and_scheme(
        destino,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    )
    return destino if destino and ok else "index"


def cadastrar(request):
    if request.user.is_authenticated:
        return redirect("index")

    destino = request.POST.get("next") or request.GET.get("next") or ""
    form = CadastroForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        usuario = form.save()
        login(request, usuario)
        return redirect(_destino_seguro(request, destino))

    return render(request, "contas/cadastrar.html", {"form": form, "next": destino})
