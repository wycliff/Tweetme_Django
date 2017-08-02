#NB: The `urlpatterns` list routes URLs to views 
#import views 
#from .views import tweet_detailed_view,tweet_list_view
from .views import TweetDetailView, TweetListView

from django.conf.urls import url

urlpatterns = [
    
    #for the function based views 
    #url(r'^$', tweet_list_view, name= "list"),
    #url(r'^1/$', tweet_detailed_view, name= "detail"),

    #using class based views 
	url(r'^$', TweetListView.as_view(), name= "list"),  # $ shows the endof the URL , hence here /tweet/
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view() , name= "detail"),  # /tweet/1/ 
]



