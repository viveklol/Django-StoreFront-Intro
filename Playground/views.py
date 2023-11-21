from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Request -> Response
# Request Handler

def say_hello(request):
    # Pull data from db
    # Transform data
    # Send email
    return HttpResponse('Hello World')