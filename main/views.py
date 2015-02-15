from django.shortcuts import render, render_to_response

def mainpage(request):
	return render_to_response('main/mainpage.html',{})
# Create your views here.
