from django.shortcuts import render


# Create your views here.
def home_view(request, **kwargs):
    return render(request, "index.html", {})
