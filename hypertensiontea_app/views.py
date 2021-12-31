from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.sessions.models import Session
from .forms import ContactForm
import os
from decouple import config

# Create your views here.
def index(request):
	return redirect('hypertension_tea')
	
def hypertension_tea(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			fullname = form.cleaned_data['fullname']
			phone_no = form.cleaned_data['phone_no']
			contact_email = form.cleaned_data['email']
			address = form.cleaned_data['address']
			product_quantity = form.cleaned_data['quantity']

			# store fullname in session
			request.session['fullname'] = fullname

			#contact_message = f"{fullname} has sent you a new message."
			contact_message = f'Hello David, \n\n' \
				f'You have a message from {fullname} with details below. \n\n' \
				f'Phone Number: {phone_no} \n' \
				f'Address: {address} \n' \
				f'Email: {contact_email} \n' \
				f'The product quantity is: {product_quantity}.'

			email_msg = EmailMessage(
        		subject='A New Message From 24Hours NG - Hypertension Tea', body=contact_message, 
        		from_email=contact_email,
			to=['testdamilare@gmail.com']
         		#to=[settings.EMAIL_HOST_USER],
        		headers={'Reply-To': contact_email})
			email_msg.send()
			#messages.success (request, f'Thank you for contacting us!.')
			return redirect ('thankyou')
	else:
		form = ContactForm()
	return render(request, 'index.html', {'form':form})


def thankyou(request):
	name = request.session['fullname']
	return render(request, 'thankyou.html', {'name':name})
