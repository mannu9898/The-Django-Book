from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import Template, Context
from books.models import Book
from books.forms import ContactForm,PublisherForm
from django.core.mail import send_mail
# Create your views here.




def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(title__icontains=query) |
			Q(authors__first_name__icontains=query) |
			Q(authors__last_name__icontains=query)
			)
		results = Book.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("search.html", {
		"results": results,
		"query": query
		})



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			topic = form.clean_data['topic']
			message = form.clean_data['message']
			sender = form.clean_data.get('sender', 'noreply@example.com')
			send_mail(
				'Feedback from your site, topic: %s' % topic,
				message, sender,
				['administrator@example.com']
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm()
	return render_to_response('contact.html', {'form': form})



def addPublisher(request):
	if request.method == 'POST':
		form = PublisherForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('add_publisher/thanks/')
		else:
			form = PublisherForm()
			return render_to_response('addPublisher.html',{'form':form})
	else:
		return render_to_response("addPublisher.html", {"Error":'Not valid username'})

def add_publisher(request):
	if request.method == 'POST':
		form = PublisherForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/addPublisher/thanks/')
		else:
			form = PublisherForm()
			return render_to_response('addPublisher.html', {'form': form})
	else:
		return render_to_response("addPublisher.html", {"Error":'Not valid username'})
