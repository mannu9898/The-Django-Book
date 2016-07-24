from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render_to_response
from books.views import search,contact,add_publisher


def current_datetime(request):
	now = datetime.datetime.now()
	here = 5
	#t = get_template('current_datetime.html')
	#html = t.render(Context({'current_date':now}))
	#return HttpResponse(html)
	return render_to_response('current_datetime.html',{'current_date':now,'var':here})

def hours_ahead(request,offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.datedelta(hours=offset)
	return render_to_response('hours_ahead.html',{'futureTime':dt,'offset':offset})

def home(request):
	var="Hello World";
	return render_to_response('index.html',{"hello":var})
