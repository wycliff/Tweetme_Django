#NB: The `urlpatterns` list routes URLs to views 
#import views 
#from .views import tweet_detailed_view,tweet_list_view  --> these are for function based views 
from .views import (
	TweetCreateView,
	TweetDeleteView,
	TweetDetailView,
	
	 TweetListView,
	 TweetUpdateView
	 )


from django.conf.urls import url

urlpatterns = [
    
    #**************for the function based views **
    #url(r'^$', tweet_list_view, name= "list"),
    #url(r'^1/$', tweet_detailed_view, name= "detail"),

    #using class based views 
	url(r'^$', TweetListView.as_view(), name= "list"),  # $ shows the endof the URL , hence here /tweet/
	url(r'^create/$', TweetCreateView.as_view(), name= "create"), #/tweet/create/
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view() , name= "detail"),  # /tweet/1/ 
    url(r'^(?P<pk>\d+)/update/$',TweetUpdateView.as_view() , name= "update"), #/tweet/1/update/
    url(r'^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view() , name= "delete"), #/tweet/1/delete/

]

		

