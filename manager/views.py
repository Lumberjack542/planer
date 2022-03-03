from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from manager.models import Comments, Marks, Product


class Planer(View):
    def get(self, request):
        context = {"product": Product.objects.all()}
        return render(request, 'title_planers.html', context)