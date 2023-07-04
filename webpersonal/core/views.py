from django.shortcuts import render, HttpResponse

htlm_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Porfolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>
"""


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contacto(request):
    return render(request, "core/contacto.html")
