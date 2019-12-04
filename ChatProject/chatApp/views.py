from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from chatApp.models import (
    Message,
    NewsArticle
)
from .forms import MessageForm
import json
from newsapi.newsapi_client import NewsApiClient
import math



newsapi = NewsApiClient(api_key='9de361c46fc54ac79cab430aaeb7ba9a')

# Create your views here.
def index(request, page=1):
    print("Entre a index")
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
    messages = Message.objects.all().order_by('pub_date').reverse()
    print("page: ", page)
    print(len(messages))
    messages = messages[0:100]
    print(len(messages))
    page = int(page)
    total_pages = math.ceil(len(messages)/5)

    messages = messages[5*page-5 : 5*page]
    pages=[]
    
    if (page<=3):
        for i in range(1,total_pages+1):
            if i <= 5:
                pages.append(i)
    elif (page >= total_pages-2):
        pages = [total_pages-4, total_pages-3, total_pages-2, total_pages-1, total_pages]
    else:
        pages = [ page-2, page-1, page, page+1, page+2]
    

    
    data = {'messages': messages,
    'messages_amount': len(messages),
    'form': form,
    'pages': pages,
    'page': page}

    return render(request, 'home.html', data)

def news(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        response = newsapi.get_everything(q=title)
        news_dict = response['articles'][:3]
        news = list(map(lambda x: NewsArticle(x), news_dict))
        data = {'news': news,}
    else:
        redirect(index)
    return render(request, 'news.html', data)