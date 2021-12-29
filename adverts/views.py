from django.shortcuts import render
from django.http import HttpResponse
from .models import Advert

def adverts(request):
	adverts = Advert.objects.all()
	context = { 'adverts':adverts }
	return render(request, 'adverts/index.html', context)

def advert_detail(request, pk):
	Advert.objects.get(pk=pk)
	context = { 'advert':advert }
	return render(request, 'adverts/advert_detail.html', context)
