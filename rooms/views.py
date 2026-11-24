from django.shortcuts import render
from .models import Room


def archive(request):
    """Список всех номеров."""
    posts = Room.objects.all().order_by('-created_date')
    return render(request, 'archive.html', {"posts": posts})
