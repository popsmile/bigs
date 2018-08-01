from django.shortcuts import render
from django.http import HttpResponse

from .models import StockCard

# Create your views here.
def index(request):
	stocks = StockCard.objects.all()
	context = {'stocks':stocks}
	return render(request, 'stocks/index.html', context)