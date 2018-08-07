from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import StockCard
from .forms import SignUpForm

# Create your views here.
def index(request):
	stocks1 = StockCard.objects.filter(category="단기후보주")
	stocks2 = StockCard.objects.filter(category="스윙")
	stocks3 = StockCard.objects.filter(category="중장기")
	stocks4 = StockCard.objects.filter(category="테마주")
	context = {'stocks1':stocks1, 'stocks2':stocks2, 'stocks3':stocks3, 'stocks4':stocks4}
	return render(request, 'stocks/index.html', context)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return render(request, 'registration/signup_done.html', {'username':username})
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form':form})

def stockpage(request, stockname):
	stock = StockCard.objects.get(name=stockname)
	context = {'stock':stock}
	return render(request, 'stocks/stockpage.html', context)