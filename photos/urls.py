from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index, name="home"),
    url(r'^search/',views.search_category,name='search_category')
]
