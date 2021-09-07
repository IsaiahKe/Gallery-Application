from photos.models import Category, Location, Pic
from django.shortcuts import render
from django.http import Http404, request
def index(request):
    title="Homepage"
    photos=Pic.get_all()
    locations=Location.get_location()
    print(photos)
    return render(request,'home.html',{'pics':photos,'title':title,'locations':locations,})

def search_category(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get("category")
        results = Pic.search_category(search_term)
        message = f"{search_term}"
        cat=Category.objects.all()
        return render(request,'category.html',{'items':results,'message':message,'cats':cat})
    else:
        message="The category is not Availabe"
        return render(request,'category.html',{'message':message})