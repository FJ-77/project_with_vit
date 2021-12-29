from django.shortcuts import render
from .models import Advert

def index(request):
	adverts = Advert.objetcs.all()
	context = { 'adverts':adverts }
	return render(request, 'adverts/index.html', context)



