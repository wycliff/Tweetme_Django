# from django import forms
# from django.forms.utils import ErrorList
from django.shortcuts import render,get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin #help redirect non-registered users

#for class based views/ generic display views 
from django.views.generic import (

								CreateView,
								DeleteView,
								DetailView,
								ListView ,
								UpdateView  
								)

from .mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import TweetModelForm
from .models import Tweet

#for the delete view 
from django.urls import reverse_lazy



# CRUD methods are handled here... 

#1)  ******* CREATE *********
class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/Create_view.html'
	success_url = "/tweet/create/"	

	#login_url = '/admin/' # LoginRequiredMixin for admin user.

    # now being done in the mixin 
	# def form_valid(self, form):
	# 	if self.request.user.is_authenticated(): # dont allow submit if user is not authenticated.
	# 		form.instance.user = self.request.user
	# 		return super(TweetCreateView, self).form_valid(form)
	# 	else:
	# 		form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"]) # confirm login status of the user 
	# 		return self.form_invalid(form)


#============ Create Using a function-baseed view ===========
# def twee_create_view(request):
# 	form = TweetModelForm(request.POST or None)

# 	if form.is_valid():
# 		instance = form.save(commit = False)
# 		instance.user = request.user
# 		instance.save()
# 	context = {
 
#       "form":form  

# 	}

# 	return render(request, 'tweets/create_view.html',context)





   
#2) ******** RETRIEVE **********
#======================== Retrive using class based views =========================================

class TweetDetailView(DetailView):
	#template_name = "tweets/detail_view.html" #not needed when the default templates are used 
	queryset = Tweet.objects.all()

	# def get_object(self):
	# 	print(self.kwargs)
	# 	#pk = self.kwargs["pk"] 
	# 	pk = self.kwargs.get("pk") #gives you the key-value pair
	# 	#return Tweet.objects.get(id = pk) #getting 
	# 	obj = get_object_or_404(Tweet , pk =pk )
	# 	return obj

 
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


#3)*************** UPDATE ************
# Though i may not use this in the tweetme app. 
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	success_url = "/tweet/"
	template_name = 'tweets/update_view.html'


#4) *************** DELETE *********
class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('home')    # takes you back home after you delete.
