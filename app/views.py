from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

job_title = [
    'Job1 Title',
    'Job2 Title',
    'Job3 Title',
]

job_desc = [
    'Job1 Description',
    'Job2 Description',
    'Job3 Description',
]

# def job_page(request):
#     my_str = '<ul>'
#     for j in job_title:
#         my_str += f'<a href=<li>{job_title[j.index]}</li>'

def job_detail_page(request, id):
    try:
        if id == 0:
            return redirect(reverse('main_page'))
        
        return_html = f'<h1>{job_title[id]}</h1> <h3>{job_desc[id]}</h3>'
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound('<h2>Page Not Found</h2>')