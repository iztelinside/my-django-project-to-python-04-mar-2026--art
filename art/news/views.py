from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView

from .forms import ArtForm
from .models import Art

class NewsDetailView(DetailView):
    model = Art
    template_name = "news/details.html"
    context_object_name = "article"

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




