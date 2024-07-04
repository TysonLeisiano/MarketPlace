from django.shortcuts import render

from item.models import Item, Category
from.forms import SignupForm


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html',
    {
        'categories': categories,
        'items': items,
    })



def contact(request):
    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')


def privacy(request):
    return render(request, 'core/privacy.html')


def terms(request):
    return render(request, 'core/terms.html')

def signup(request):
    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })