from django.shortcuts import render
from django.shortcuts import render_to_response
from menu.models import Restaurant,Food

# Create your views here.

def menu(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('menu.html',locals())