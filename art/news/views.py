from django.shortcuts import render
from .models import Art

# Create your views here.

def news(request):
    arts = Art.objects.order_by("title")
    return render(request, "news/news.html", {
        "arts": arts,
        "debug": "VIEW IS WORKING"
    })


# def news(request):
#     arts = Art.objects.all()
#     return render(request, "news/news.html", {
#         "arts": arts,
#         "test": "WORKING"
#     })
