"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

#Creating a URL end point for serving static files	
from django.conf import settings
from django.conf.urls.static import static

#import views 
from .views import home 

urlpatterns = [
    url(r'^admin/', admin.site.urls), # /admin/
    url(r'^$', home, name= "home"), #/
     url(r'^tweet/', include('tweets.urls', namespace = 'tweet')), 

    #Wrapping whole list of urls from tweets app into this main one  
]


#in oder to serve static files*
if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)) 
