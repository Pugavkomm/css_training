from django.shortcuts import render
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "timeline/timeline_index.html")
