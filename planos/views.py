from django.shortcuts import render

from .models import PacoteRepublica, Plano

ABAS = ("individual", "republica")


def lista(request):
    aba = request.GET.get("aba", "individual")
    if aba not in ABAS:
        aba = "individual"

    contexto = {
        "planos": Plano.objects.all(),
        "pacotes": PacoteRepublica.objects.all(),
        "aba": aba,
    }
    return render(request, "planos/lista.html", contexto)
