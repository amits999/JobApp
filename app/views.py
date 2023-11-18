from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def job_detail_page(request, id):
    return HttpResponse(f'Job detail page: {id}')