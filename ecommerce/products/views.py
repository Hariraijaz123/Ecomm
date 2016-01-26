from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

# Create your views here.
def view1(request):
    templates = "home.html"
    return render(request, templates, {})


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class VariationListView(ListView):
    model = Product

class CategoryListView(ListView):
    model = Product

class CategoryDetailView(DetailView):
    model = Product


