from django.shortcuts import render, HttpResponse
import requests
API_KEY = '9c82badaf452409db67d5d83ee66a05e'
# Create your views here.


def home(request):
    country=request.GET.get('country')
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    news = data['articles']
    context = {
        'news': news
    }
    return render(request, 'home.html', context)
