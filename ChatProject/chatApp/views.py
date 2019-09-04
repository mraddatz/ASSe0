from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse, render_to_response
from chatApp.models import (
    Message,
    NewsArticle
)
from .forms import MessageForm
import json
import math




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

