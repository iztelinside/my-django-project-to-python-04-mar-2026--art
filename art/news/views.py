from django.shortcuts import render

from .forms import ArtForm
from .models import Art

# Create your views here.

def news(request):
    arts = Art.objects.order_by("title")
    return render(request, "news/news.html", {
        "arts": arts,
        "debug": "VIEW IS WORKING"
    })

def create(request):
    form = ArtForm(request.POST or None)
    data = {
        "form": form,
    }
    return render(request, "news/create.html", data)



