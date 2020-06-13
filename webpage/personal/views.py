from django.shortcuts import render

def index(request):
    return render(request, 'personal/index.htm')

def contact(request):
    return render(request, 'personal/contact.htm', {'content':['if you want to contact me email','atharvas@rocketmail.com']})

