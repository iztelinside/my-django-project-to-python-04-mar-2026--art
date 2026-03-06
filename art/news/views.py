from django.shortcuts import render, redirect

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
    error = ""

    if request.method == "POST":
        form = ArtForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('news')   # имя url
        else:
            error = "Форма неверная"

    form = ArtForm()

    data = {
        "form": form,
        "error": error
    }

    return render(request, "news/create.html", data)




