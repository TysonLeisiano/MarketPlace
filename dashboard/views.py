from django.shortcuts import render, get_object_or_404

# Create your views here.
from item.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    for item in items:
        if item.image and hasattr(item.image, 'url'):
            image_url = item.image.url
        else:
            image_url = 'dashboard/toy2.jpg'

    return render(request, 'dashboard/index.html', {
        'items': items,
    })


