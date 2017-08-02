from django.shortcuts import render,get_object_or_404
from .models import Tweet
#for class based views/ generic display views 
from django.views.generic import DetailView, ListView 

# CRUD methods are handled here... 


#1) ******** RETRIEVE **********
#======================== Retrive using class based views =========================================

class TweetDetailView(DetailView):
	#template_name = "tweets/detail_view.html" #not needed when the default templates are used 
	queryset = Tweet.objects.all()

	def get_object(self):
		print(self.kwargs)
		#pk = self.kwargs["pk"] 
		pk = self.kwargs.get("pk") #gives you the key-value pair
		#return Tweet.objects.get(id = pk) #getting 
		obj = get_object_or_404(Tweet , pk =pk )
		return obj

 
class TweetListView(ListView):
	#template_name = "tweets/list_view.html"
	queryset = Tweet.objects.all()

	def get_context_data(self, *args,**kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)

		#context["another_list"] = Tweet.objects.all() # specifying a new context
		print(context)
		return context


#======================== Retrieve, using function-based views ========================================
# def tweet_detailed_view(request,pk = pk ): pk == id 
# 	#obj = Tweet.objects.get(id = id)  # Get from the database.
#   obj = get_object_or_404(Tweet , pk =pk )
# 	context = {
#         "object":obj
#         }
# 	return render(request,"tweets/detail_view.html", context) #{} empty dictionary for context. Detail of a paricular tweet

 
# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	print(queryset)
#     #The particular DB context passed 
# 	context = {
#         "object_list" : queryset
#         }
# 	return render(request,"tweets/list_view.html", context) # import in urls and wrap to them. Go to the template to see what happens

# =============  Some notes =======================================================================
#There may be a templates folder in every app 
#Tres Important: Views load templates, `urlpatterns` list routes URLs to views. Models- our DB- is then 
#Queried in views.py
#===================================================================================================
