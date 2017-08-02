from django.shortcuts import render

#Here we can either use class-based views or function-based views.

#retrieve
# GET --template home,html.
def home(request):
	return render(request,"home.html",{}) # render (request, template , context)


	

