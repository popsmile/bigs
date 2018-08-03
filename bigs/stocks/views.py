from django.shortcuts import render
from django.http import HttpResponse

from .models import StockCard

# Create your views here.
def index(request):
	stocks1 = StockCard.objects.filter(category="단기후보주")
	stocks2 = StockCard.objects.filter(category="스윙")
	stocks3 = StockCard.objects.filter(category="중장기")
	stocks4 = StockCard.objects.filter(category="테마주")
	context = {'stocks1':stocks1, 'stocks2':stocks2, 'stocks3':stocks3, 'stocks4':stocks4}
	return render(request, 'stocks/index.html', context)

def stockcard(request):
	stocks1 = StockCard.objects.filter(category="단기후보주")
	stocks2 = StockCard.objects.filter(category="스윙")
	stocks3 = StockCard.objects.filter(category="중장기")
	stocks4 = StockCard.objects.filter(category="테마주")
	context = {'stocks1':stocks1, 'stocks2':stocks2, 'stocks3':stocks3, 'stocks4':stocks4}
	return render(request, 'stocks/stockcard.html', context)