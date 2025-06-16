from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def business_growth(request):
    return render(request, 'core/business_growth.html')

def talent_growth(request):
    return render(request, 'core/talent_growth.html')

def how_it_works(request):
    return render(request, 'core/how_it_works.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
