from django.shortcuts import render

# Create your views here.


def index(request):
    tags = [
        "python",
        "Flask",
        "Django",
        "HTML",
        "SQLAlchemy",
    ] * 3
    context = {
        "tags": tags,
    }
    return render(request, "timeline_2/timeline_2_index.html", context)
